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

    while True:
        port = input('Введите порт: {} '.format(cam.objects[id]['ports']))

        if port in cam.objects[id]['ports']:
            return port
        else:
            print('Ошибка, некорректный порт')


def check_video(id, port):
    vlc = ''

    if cam.objects[id]['rtsp'] == 'rtsp1':
        vlc = f"vlc {cam.rtsp.get('rtsp1')}{cam.objects[id]['ip']}:{port}"

    elif cam.objects[id]['rtsp'] == 'rtsp2':
        vlc = f"vlc rtsp://{cam.objects[id]['ip']}:{port}{cam.rtsp.get('rtsp2')}"

    elif cam.objects[id]['rtsp'] == 'rtsp3':
        vlc = 'vlc "rtsp://{}:{}{}"'.format(cam.objects[id]['ip'], port, cam.rtsp.get('rtsp3'))

    elif cam.objects[id]['rtsp'] == 'rtsp4':
        vlc = f"vlc {cam.rtsp.get('rtsp4')}{cam.objects[id]['ip']}:{port}"

    elif cam.objects[id]['rtsp'] == 'rtsp5':
        vlc = f"vlc {cam.rtsp.get('rtsp5')}{cam.objects[id]['ip']}:{port}"

    os.system(vlc)


if __name__ == '__main__':
    id_object = check_err_id_object()
    while True:
        port = check_err_port(id_object)
        check_video(id_object, port)
