import hashlib
import time

import requests

from config.config import headers, cookies
from decrypt.decrypt import decrypt


def sign(text: str) -> str:
    md5 = hashlib.md5()
    md5.update(text.encode())
    return md5.hexdigest()


def translate(word: str, key: str) -> str:
    """
    translate api
    :param word: 单词
    :param key: md5 str
    :return: aes加密后的urlsafe_base64
    """
    now = str(int(time.time() * 1000))
    source_text = f'client=fanyideskweb&mysticTime={now}&product=webfanyi&key={key}'
    data = {
        'i': word,
        'from': 'auto',
        'to': '',
        'useTerm': 'false',
        'dictResult': 'true',
        'keyid': 'webfanyi',
        'sign': sign(source_text),
        'client': 'fanyideskweb',
        'product': 'webfanyi',
        'appVersion': '1.0.0',
        'vendor': 'web',
        'pointParam': 'client,mysticTime,product',
        'mysticTime': now,
        'keyfrom': 'fanyi.web',
        'mid': '1',
        'screen': '1',
        'model': '1',
        'network': 'wifi',
        'abtest': '0',
        'yduuid': 'abcdefg',
    }
    response = request.post('https://dict.youdao.com/webtranslate', data=data)
    return response.text


def get_aes_key():
    '''获取md5和aes的key'''
    response = request.get(
        'https://dict.youdao.com/webtranslate/key?keyid=webfanyi-key-getter&sign=655a32a1b8cc81849d9d65d750d90b06&client=fanyideskweb&product=webfanyi&appVersion=1.0.0&vendor=web&pointParam=client,mysticTime,product&mysticTime=1728921421837&keyfrom=fanyi.web&mid=1&screen=1&model=1&network=wifi&abtest=0&yduuid=abcdefg',
    )
    return response.json().get('data')


def main(word):
    keys = get_aes_key()
    assert keys, '接口变动'
    result = translate(word, keys['secretKey'])
    # key, iv = create_key_iv(keys['aesKey'], keys['aesIv'])
    result = decrypt(result)
    print(result)


if __name__ == '__main__':
    request = requests.Session()
    request.cookies.update(cookies)
    request.headers = headers
    word = '惊喜'
    main(word)
