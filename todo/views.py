from django.shortcuts import render
from django.http import Http404

# import class Task dari file todo/models.py
from .models import Task
from .forms import TaskForm

# Membuat View untuk halaman daftar task
def index_view(request):
    # Mengambil semua data task
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    # parsing data task ke template todo/index.html dan merender nya
    return render(request, 'todo/index.html', context)


# Membuat View untuk halaman detail task
def detail_view(request, task_id):
    # Mengambil data task berdasarkan task ID
    try:
        task = Task.objects.get(pk=task_id)
        context = {
            'task': task
        }
    except Task.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Task tidak ditemukan.")
    # parsing data task ke template todo/detail.html dan merendernya
    return render(request, 'todo/detail.html', context)


# Membuat View untuk halaman form tambah task
def create_view(request):
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        # membuat objek dari class TaskForm
        form = TaskForm(request.POST)
        # Mengecek validasi form
        if form.is_valid():
            # Membuat Task baru dengan data yang disubmit
            new_task = TaskForm(request.POST)
            # Simpan data ke dalam table tasks
            new_task.save()
            # mengeset pesan sukses dan redirect ke halaman daftar task
            messages.success(request, 'Sukses Menambah Task baru.')
            return redirect('todo:index')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class TaskForm
        form = TaskForm()
    # merender template form dengan memparsing data form
    return render(request, 'todo/form.html', {'form': form})

def create_view(request):
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        # membuat objek dari class TaskForm
        new_task = TaskForm(request.POST)
        # Mengecek validasi form
        if new_task.is_valid():
            # Simpan data ke dalam table tasks
            new_task.save()
            # mengeset pesan sukses dan redirect ke halaman daftar task
            messages.success(request, 'Sukses Menambah Task baru.')
            return redirect('todo:index')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class TaskForm
        form = TaskForm()
        # merender template form dengan memparsing data form
        return render(request, 'todo/form.html', {'form': form})

# Membuat View untuk halaman form ubah task
def update_view(request, task_id):
    try:
        # mengambil data task yang akan diubah berdasarkan task id
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Task tidak ditemukan.")
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            # Simpan perubahan data ke dalam table tasks
            form.save()
            # mengeset pesan sukses dan redirect ke halaman daftar task
            messages.success(request, 'Sukses Mengubah Task.')
            return redirect('todo:index')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class TaskForm
        form = TaskForm(instance=task)
    # merender template form dengan memparsing data form
    return render(request, 'todo/form.html', {'form': form})
    
# Membuat View untuk menghapus data task
def delete_view(request, task_id):
    try:
        # mengambil data task yang akan dihapus berdasarkan task id
        task = Task.objects.get(pk=task_id)
        # menghapus data dari table tasks
        task.delete()
        # mengeset pesan sukses dan redirect ke halaman daftar task
        messages.success(request, 'Sukses Menghapus Task.')
        return redirect('todo:index')
    except Task.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Task tidak ditemukan.")