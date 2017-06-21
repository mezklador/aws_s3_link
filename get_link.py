import json

from redis import Redis


r = Redis(db=3)


def getS3link():
    try:
        res = r.get('s3link')

        if res is not None:
            json_res = dict(url=res.decode('utf-8'))
        else:
            json_res = dict(url='')
    except:
        json_res = dict(error={'code': 5,
                               'msg': 'Cannot access to db.'})
    finally:
        return json_res


if __name__ == '__main__':
    print(getS3link())
