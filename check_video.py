import cam_objects as cam
import os


def check_err_id_object():
    while True:
        id_object = input('Введите номер объекта: ')
        if cam.objects.get(id_object):
            print(f"Объект: {cam.objects[id_object]['name']}")
            return id_object
        else:
            print('Ошибка, объект не найден')
            continue


def check_err_port(id):
    port2 = cam.objects[id].get('port2')

    while True:
        port = input('{}{} Введите порт: '.format(cam.objects[id]['ports'], port2))

        if port in cam.objects[id]['ports']:
            return port
        elif port in cam.objects[id]['port2']:
            return port
        elif port.lower() == 'q':
            check_err_id_object()
        else:
            print('Ошибка, некорректный порт')


def check_video(id, port):

    if port in cam.objects[id]['port2']:
        link = cam.objects[id]['rtsp2'].format(cam.objects[id]['ip'], port)
        vlc = f"vlc {link}"

    else:
        link = cam.objects[id]['rtsp'].format(cam.objects[id]['ip'], port)
        vlc = f"vlc {link}"

    os.system(vlc)


if __name__ == '__main__':
    id_object = check_err_id_object()
    while True:
        port = check_err_port(id_object)
        check_video(id_object, port)
