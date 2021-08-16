from django.shortcuts import redirect, render
from rest_framework.views import APIView
from .models import Pattern,Boss
from .form import PatternForm
# Create your views here.


def make_title(guide):
    boss=guide.boss
    phase=guide.phase
    mode=guide.mode
    title=boss+' '+mode+' 모드 - '+phase+' 페이즈'
    return title

class HomePage(APIView):

    def get(self,request):
        guides=Pattern.objects.all()
        titles=[]
        for guide in guides:
            boss_id=guide.id
            title=make_title(guide)
            data={'boss_id':boss_id,'title':title}
            titles.append(data)

        titles.sort(key=lambda x:x['title'])
        return render(request,'home.html',context={'titles':titles})
    
class GuideCreate(APIView):


    def get(self,request):
        form=PatternForm()
        return render(request,'create.html',context={'form':form})
        # bosses=Boss.objects.all()
        # bosses=[boss.boss for boss in bosses]
        # print(bosses)
        # modes=['노말','하드','헬','리허설','어비스']
        # phases=['1','2','3','4','5','6','7']
        # return render(request,'create.html',context={'bosses':bosses,'modes':modes,'phases':phases})
    def post(self,request):
        boss=request.data.get('boss')
        mode=request.data.get('mode')
        phase=request.data.get('phase')
        guide=request.data.get('guide')

        pattern=Pattern.objects.create(boss=boss,mode=mode,phase=phase,guide=guide)
        pattern.save()

        return redirect('home')

class GuideSelect(APIView):
    def get(self,request,boss_id):
        print('Guide GET',boss_id)
        guide=Pattern.objects.get(id=boss_id)
        print(guide)
        title=make_title(guide)
        guide=guide.guide
        return render(request,'guide.html',context={'title':title,'guide':guide})
        
