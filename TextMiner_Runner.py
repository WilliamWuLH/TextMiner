import os

def run_app():
    # Environment configuration
    success = False
    try:
        os.system('python --version')
        os.system('pip --version')
        os.system('pip install streamlit==0.72.0')
        os.system('pip install pandas==0.25.3')
        os.system('pip install numpy==1.19.3')
        os.system('pip install jieba==0.42.1')
        os.system('pip install snownlp==0.12.3')
        os.system('pip install matplotlib==3.1.1')
        os.system('pip install wordcloud==1.8.1')
    except Exception as e:
        print('Exception : ', e)
        return
    else:
        print('\n-------> Environment configuration is successful!')
        success = True
    
    if success:
        # run app
        try:
            os.system('streamlit run Text_Miner.py')
        except Exception as e:
            print('Error:', e)
            return

if __name__ == "__main__":
    run_app()