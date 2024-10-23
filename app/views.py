from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from datetime import date
from django.core.mail import send_mail
from django.http import FileResponse, Http404, JsonResponse
import secrets
import string
from django.contrib.auth.models import User

def Index(request):
    thrusts = Thrust.objects.all()
    context = {"thrusts":thrusts, "nb_thrusts":len(thrusts)}
    return render(request, 'index.html', context)


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('library')
    return render(request, 'login.html')


@login_required
def Logout(request):
    logout(request)
    return redirect('login')


def Join_us(request):
    return render(request, 'join_us.html')


def News_Events(request):
    news = NewsEvent.objects.filter(Type="News")
    today = date.today()
    past_events = NewsEvent.objects.filter(Date__lt=today, Type="Event")
    future_events = NewsEvent.objects.filter(Date__gte=today, Type="Event")
    context = {"news":news, "past_events":past_events, "future_events":future_events}
    return render(request, 'news_events.html', context)


def Library(request):
    publications = Publication_Elearning.objects.filter(Type="Publication")
    elearning = Publication_Elearning.objects.filter(Type="E-learning")
    seminars_webinars = Seminars_Webinars_Podcast.objects.filter(Type="Seminars & Webinars")
    podcasts = Seminars_Webinars_Podcast.objects.filter(Type="Podcast")
    context = {"publications":publications, "elearning":elearning,
               "seminars_webinars":seminars_webinars, "podcasts":podcasts}
    return render(request, 'library.html', context)


def Resource(request):
    equipments = Pooling_Equipment.objects.all()
    context = {"equipments":equipments}
    return render(request, 'resource.html', context)


def Members(request):
    members = Member.objects.filter(Role="member")
    context = {"members":members, "title":"Our Team"}
    return render(request, "members.html", context)


def Governance(request):
    members = Member.objects.filter(Role="governance")
    super_members = [m for m in members if m.Second_Name.upper() in ["ALAMI", "EL HABTI"]]
    members = [m for m in members if m not in super_members]
    context = {"members":members, "super_members":super_members, "title":"Governance"}
    return render(request, "members.html", context)


def Management(request):
    members = Member.objects.filter(Role="management")
    context = {"members":members, "title":"Management"}
    return render(request, "members.html", context)


def send_confirmation_email(request):
    first_name = request.POST.get('first_name')
    email = request.POST.get('email')
    confirmation_email_txt = open("static/emails/confirmation_email.txt", "r").read().format(first_name)
    subject = 'Confirmation Email'
    from_email = 'boutasknitesoufiane@gmail.com'
    recipient_list = [email]
    send_mail(subject, confirmation_email_txt, from_email, recipient_list)


def send_acceptation_email(application, username, password):
    first_name = application.First_Name
    email = application.Email
    email_body = open("static/emails/acceptation_email.txt", "r").read().format(first_name, username, password)
    subject = 'Congratulations! Your Application Has Been Accepted'
    from_email = 'boutasknitesoufiane@gmail.com'
    recipient_list = [email]
    send_mail(subject, email_body, from_email, recipient_list)


def send_rejection_email(application):
    first_name = application.First_Name
    email = application.Email
    email_body = open("static/emails/rejection_email.txt", "r").read().format(first_name)
    subject = 'Update on Your Application'
    from_email = 'boutasknitesoufiane@gmail.com'
    recipient_list = [email]
    send_mail(subject, email_body, from_email, recipient_list)


@csrf_exempt
def Save_Application(request):
    try:
        first_name = request.POST.get('first_name')
        second_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        affiliation = request.POST.get('affiliation')
        research_area = request.POST.get('research_area')
        position = request.POST.get('position')
        cv_file = request.FILES.get('cv')
        image = request.FILES.get('image')
        biography = request.POST.get('biography')
        motivation = request.POST.get('motivation')
        contribution = request.POST.get('contribution')
        references = request.POST.get('references')
        app = Application.objects.create(
            First_Name=first_name,
            Second_Name=second_name,
            Email=email,
            Phone_Number=phone_number,
            Affiliation=affiliation,
            CV=cv_file,
            Image=image,
            Biography=biography,
            Research_Area=research_area,
            Position=position,
            Motivation=motivation,
            Contribution=contribution,
            References=references
        )
        try:
            send_confirmation_email(request)
        except:
            app.delete()
            return JsonResponse({'msg': 'The email address you entered does not exist. Please enter a valid one.'})
        return JsonResponse({'msg': 'Success'})
    except:
        return JsonResponse({'msg': 'Something went wrong. Please try again'})


def Profile(request, id):
    member = Member.objects.get(id=id)
    context = {"member":member}
    return render(request, 'profile.html', context)


def Applications(request):
    applications = Application.objects.all()
    context = {"applications":applications}
    return render(request, 'applications.html', context)


@csrf_exempt
def ChangeStatus(request):
    application = Application.objects.get(id=int(request.POST["Id"]))
    if request.POST["Action"] == "accept":
        application.Status = "Accepted"
        Member.objects.create(
            First_Name=application.First_Name,
            Second_Name=application.Second_Name,
            Email=application.Email,
            Phone_Number=application.Phone_Number,
            Affiliation=application.Affiliation,
            CV=application.CV,
            Image=application.Image,
            Biography=application.Biography,
            Research_Area=application.Research_Area,
            Position=application.Position,
            Motivation=application.Motivation,
            Contribution=application.Contribution,
            References=application.References
        )
        username = f"{application.First_Name}.{application.Second_Name}"
        email = application.Email
        password = generate_password()
        user = User.objects.create_user(username=username, email=email, password=password)
        Member.User_Id = user.id
        send_acceptation_email(application, username, password)
    else:
        application.Status = "Rejected"
        send_rejection_email(application)
    application.save()
    return HttpResponse("ok")


def News_or_Event(request, id):
    news_or_event = NewsEvent.objects.get(id=id)
    context = {"news_or_event":news_or_event}
    return render(request, "news_or_event.html", context)


def serve_pdf(request, document_id):
    try:
        Document_File = Publication_Elearning.objects.get(id=document_id)
        response = FileResponse(Document_File.File.open(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{Document_File.File.name}"'
        return response
    except Member.DoesNotExist:
        raise Http404("PDF document not found")


def generate_password():
    length = 8
    characters = string.ascii_lowercase
    characters += string.digits
    characters += string.ascii_uppercase
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password
