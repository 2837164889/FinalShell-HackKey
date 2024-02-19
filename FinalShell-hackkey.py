import hashlib
#最高支持到V3.9.5.4版本
def main():
    print("请输入FinalShell的离线机器码：")
    machine_code = input()
    generate_key(machine_code)

def generate_key(hardware_id):
    pro_key = transform(str(61305) + hardware_id + str(8552)) #高级版
    pf_key = transform(str(2356) + hardware_id + str(13593)) #专业版
    print("请将下面两行(任意一行)复制到离线激活中：" 
          + "\n高级版激活码为："+pro_key 
          + "\n专业版激活码为："+pf_key ) 

def transform(s):
    md5_hash = hash_md5(s)
    return md5_hash[8:24]

def hash_md5(s):
    hashed = hashlib.md5(s.encode()).hexdigest()
    return hashed

if __name__ == "__main__":
    main()
