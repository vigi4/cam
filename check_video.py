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
        port = input('{}{} Введите порт: '.format(cam.objects[id]['ports'], cam.objects[id].get('port2')))
        try:
            if port in cam.objects[id]['ports']:
                return port
            elif port.lower() == 'q':
                main()
            elif port in cam.objects[id].get('port2'):
                return port
        except:
            print('Ошибка, некорректный порт')


def check_video(id, port):
    vlc = ''

    if port in cam.objects[id]['ports']:
        link = cam.objects[id]['rtsp'].format(cam.objects[id]['ip'], port)
        vlc = f"vlc {link}"

    elif port in cam.objects[id]['port2']:
        link = cam.objects[id]['rtsp2'].format(cam.objects[id]['ip'], port)
        vlc = f"vlc {link}"

    os.system(vlc)


def main():
    id_object = check_err_id_object()

    while True:
        port = check_err_port(id_object)
        check_video(id_object, port)


if __name__ == '__main__':
    main()
