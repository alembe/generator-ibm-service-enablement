from ibm_cloud_env import IBMCloudEnv
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    username=IBMCloudEnv.getString('watson_tone_analyzer_username'),
    password=IBMCloudEnv.getString('watson_tone_analyzer_password'),
    version='2016-05-19')

def getService(app):
    return 'watson-tone-analyzer', tone_analyzer