# import hashlib
# import base64
#
# md5 = hashlib.md5()
# md5.update('ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'.encode())
# # md5.update('client=fanyideskweb&mysticTime=1728632847083&product=webfanyi&key=fsdsogkndfokasodnaso'.encode())
# print(md5.hexdigest())
# print(base64.b64decode('Z21kD9ZK1ke6ugku2ccWu-MeDWh3z252xRTQv-wZ6jddVo3tJLe7gIXz4PyxGl73nSfLAADyElSjjvrYdCvEP4pfohVVEX1DxoI0yhm36yuAM59EzZYPvHers_Hmic0I84v4HsI9283_pdnqxFeiOFDom23KW4Dlg-Lqxu1hE7748kNaBB3D7sZOLI_m_B_SE3xK0qJipfEDVcbyPWDx0YIMYR2Lce9w64ie7uJa-JEORP6HhTwWdv9zXwT8NOQboN7WSfgFRv3pLnjfii4pMRp2Ey4suRw7RPoLis5JQ3PW0UFhurXWz9AoYaNFogJiieSYM9cmhjkGhpYT19MoSUg5gB2DPu2N7ueztndHvH0qubf9KmATDVhKRKOs890NZi-OTeOn-yKpN1LjOaAVGQOAkVUX5iCCOyRUjC8G5p85k7B1jWP2pHldhLIEi9PZx4TjNhXgJSM0HtqsfzfYfwj96d-PVJ72CQD0ejHOn_DLRV73Z99PIE6SjGKbqGDj52f5zQCfRyKNdXOHG10F_pMLR3AbzK4yVVjxD9th5grGXd2gw6tMNIK5oVDsRKiMRSWJ863D9LHMqiOMIsLTc-d7ED2-dsPjO61ANyTVrwHEJmUKHpsL54u6Iq9b9qWWLf8_yxI5yH8I2afFLqwVlwfOHYrG8wRFgbgFLwanw61xv4A4Dgol3PS3MLG47gotr9W5AfZMZ5ve1osz-jLwGBpFxLjw-uLyw6KWpGtJVjZakgEuEYCJ8Iz5zxRuFA_iC5mXDPERQtqHbB2VE65RVP53S18lsGH85WYjGmWwBgQoWSGG0UjjoaM63lZlS6dW7Tz_7nXPp0a-MFWsmN4K-SQ1dl8M53F2oGOOiB5i-rKZOgQaST3USpKLW6M8zSlVuQpdBEwmqziYkZsAaz-ao0-jZHA0rvcwf8GJ6x8xMIH0M-hJYdsX9eesg2ow7CLrTD3xXWs9Ykg5k0isApogi6cTO3gAnXG2d4f_r1t6j-fMThTgfjd9twLnfetTO-CFbP6NWHO7B9CDWqJf3lM3FGv43Rw3FKweLKn9qa5vB_2rpYicCJvSCxSr3TXgLujinY5Pypi5d9gIro9gRi1sEP13AE-Mta0oVNvbWVGY_VLJTqE8neQX0FPtbIypaljHJ0R53W416byBcH8BNsMd59foobwCpFEtVlP7x7YiszXNesYJVAFJhoE6ka2aCf_qCxKMJJMrFL93cHKjDCnNpBkmr-S2theUvDeBMEIsz-tb6CmFknKu-c4Cfupf_M1O1k1cw7EMW1eLuBEkOr1MMcliyd4IgOkkLCpqZUjbFRklrpIJLXOTCx3h-8voJ9Keh_ghAr537N8zU5Ntnjpz3pctkYoM0XPp3cO17wkL5JGlEvT0JdOPr38DdKkdRotW6rC-cPAMXJlLp6MZ56ohj4ocG5w46wfdqwvyGNTqY8gRSnjYMf9kQ919kdmaJlqIjosdIX18KmMXE4lMjy_-5L1A5azjERFO9QC7CZu_hDE='))

# import base64
#
# from Crypto.Cipher import AES
# from Crypto.Util.Padding import unpad
#
# key = [8, 20, 157, 167, 60, 89, 206, 98, 85, 91, 1, 233, 47, 52, 232, 56]
# iv = [210, 187, 27, 253, 232, 59, 56, 195, 68, 54, 99, 87, 183, 156, 174, 28]
# cypher = 'Z21kD9ZK1ke6ugku2ccWuz4Ip5f4PLCoxWstZf_6UUyBoy8dpWc3NOXFRrnPMya7tiupMBvZq6prfpNeRC4wBjEBpsBUOa2e-smiNf1ksxYSxE3NL-YLLqCRE4D4P-98D9Q_xqbz3DnncW6QdqvsBP9AQcIJDEvD4ixnlSbHyTJgoFOc-RS_cNV2Ahj0TuiXudHDPN32ii82p5Arq2ttYVY0lEkXcOoceTTLa9cEItYAJOK-YKwqeIKkL5mayNUzHReby3KgJbio9wC_X3B15gVHpNgftX0JbEmj5PCoj2JvdUZvn_vUrztlNycEPhnl-AAkNJ2YzKxzhulP6XF3DYPO2fR6wlc9XoMosR3vAFUYO35LRo8BuaUoVqGtVZiURGS45bYv-Z7aP6w8IjmqDMaRinv1lqIKhwj4HsebrRoACscpuSWufn8NeUjyBrRdByPwBetbCv_7tUvqiQR_HFjruRGyHXNBzxmbIQIrNKWIKSdSOiWo15DR0ozOh2NNj7S2TUBvqg59aP1_Bsg6Hn-R1xNobtXCgJqojYWN5VxqBzslxJ6Ordot0G2arsrzaYDRt_tuMz8JH2NmlYPWSXmWTcfZtPKJ7mu2lhkYg_TLNbi4hsDXwHPM70SVFxYNOSGp7PBpQ8q187dsDAgx4pfsTMuVhjYS1SOqcYHig2gqHc8Lo1Zefg31BztiamUjimYKZPnSqofQuvVUX0fP0z69pmTp6b9vXaSRxyqVzMFhmzoSWs3SmP8qAuhknVRT8KvdSDPlIhAG_iXGU6AvbhmZx7e_VmXXWAR7M_pLjph6kdCt4fwiSdeNeSa3EE2Sla3BNnCbIBTi00FXEUAvNQ=='
# aes = AES.new(bytes(key), AES.MODE_CBC, bytes(iv))
# decoded_bytes = base64.urlsafe_b64decode(cypher)
# result = aes.decrypt(decoded_bytes)
# print(unpad(result, 16))


## key encrypt

source_key = 'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'
key = source_key[21:-21]
end_ = source_key[-21:]
result = end_ + key
ascii_result = [ord(i) for i in result]
ascii_result[21] = 128
# print(ascii_result)
# print(ascii_result[:22] + ascii_result[-8:])
# J!Iv6v^6fvi2WN@bYpJ4C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBe
source_iv = 'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'
result = source_iv[-20:] + source_iv[20:-20]
result = [ord(i) for i in result]
result[20] = 128
print(result[:21] + result[-8:])

## fill
# [65, 100, 97, 90, 104, 65, 110, 120, 118, 71, 99, 67, 89, 54, 86, 89, 70, 119, 110, 72, 108, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 77, 90, 78, 51, 57, 106, 94, 68]
# print(key)
#7SIOUP2T0C9WHMZN39j^DB*RGygVywfNBwpmBaZg*WT
# ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^D
# AdaZhAnxvGcCY6VYFwnHlB*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^D
