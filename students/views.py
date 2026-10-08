from django.shortcuts import render
from .models import Student
def home(request):
    if request.method=="POST":
        # ADD STUDENT
        if "add_student" in request.POST:
            name = request.POST['name']
            age = request.POST['age']
            course = request.POST['course']
            Student.objects.create(
                name=name,
                age=age,
                course=course
            )
        # DELETE STUDENT
        elif "delete_id" in request.POST:
            delete_id=request.POST.get("delete_id")
            Student.objects.get(id=delete_id).delete()
                
        # UPDATE STUDENT
        if "update_id" in request.POST:
            update_id=request.POST.get("update_id")
            student = Student.objects.get(id=update_id)
            student.name=request.POST["name"]
            student.age=request.POST["age"]
            student.course=request.POST["course"]
            student.save()


    students=Student.objects.all()
    return render(request,'home.html',{'students':students})
