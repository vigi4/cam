import cam_objects as cam
import os


def check_err_id_object():
    while True:
        code_object = input('Введите номер объекта: ')
        if cam.objects.get(code_object):
            print(f"Объект: {cam.objects[code_object]['name']} {cam.objects[code_object]['id']}")
            return code_object
        else:
            print('Ошибка, объект не найден')
            continue


def check_err_port(id):
    while True:
        port = input('Введите порт: {} '.format(cam.objects[id]['ports']))
        if port in cam.objects[id]['ports']:
            return port
        else:
            print('Ошибка, некорректный порт')


def check_video(id, port):
    vlc = 'vlc {}{}:{}'.format(cam.objects[id]['rtsp'], cam.objects[id]['ip'], port)
    os.system(vlc)


if __name__ == '__main__':
    id = check_err_id_object()
    while True:
        port = check_err_port(id)
        check_video(id, port)
