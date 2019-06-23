output_file_location = 'C:/Users/User/Desktop/Deep l/nmt/model/output_dev_921'
tst_file_location = 'C:/Users/User/Desktop/Deep l/nmt/new_data/tst2013.from'

if __name__ == '__main__':
    with open(output_file_location,"r") as f:
        content = f.read()
        to_data = content.split('\n')

    with open(tst_file_location,"r") as f:
        content = f.read()
        from_data = content.split('\n')

    for n, _ in enumerate(to_data[:-1]):
        print(30*'_')
        print('>',from_data[n])
        print()
        print('Reply:',to_data[n])