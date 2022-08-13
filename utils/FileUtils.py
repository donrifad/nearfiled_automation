class FileUtils:

    def read_text_file(self, file_name):
        with open(file_name) as f:
            contents = f.readlines()
            return contents
            f.close()

    def write_text_file(self, results_file_name, results):
        with open(results_file_name, 'w') as f:
            f.write(f'{"Visited Coordinates":{25}} {"Results":{8}}')
            f.write('\n')
            for result in results:
                print(f'{result[0]:{25}} {result[1]:{8}}')
                f.write(f'{result[0]:{25}} {result[1]:{8}}')
                f.write('\n')
        f.close()
