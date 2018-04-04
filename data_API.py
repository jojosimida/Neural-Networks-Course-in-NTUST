import requests

class Param():
    def __init__(self,time_start="2018-04-01-0",time_end="2018-04-01-23"):

        #==========set the time argument==========
        self.time_start = time_start        
        self.time_end = time_end
        #=========================================
        
        self.path = 'D:/Program/dataset/KDD2018/'
        self.url_root = 'https://biendata.com/competition/'


        # url of data
        self.url_bj_air = self.url_root+'airquality/bj/'+self.time_start+'/'+self.time_end+'/2k0d1d8'
        self.url_bj_mete = self.url_root+'meteorology/bj/'+self.time_start+'/'+self.time_end+'/2k0d1d8'
        self.url_bj_grid = self.url_root+'meteorology/bj_grid/'+self.time_start+'/'+self.time_end+'/2k0d1d8'
        self.url_ld_air = self.url_root+'airquality/ld/'+self.time_start+'/'+self.time_end+'/2k0d1d8'
        self.url_ld_grid = self.url_root+'meteorology/ld_grid/'+self.time_start+'/'+self.time_end+'/2k0d1d8'


        # path of data
        self.path_bj_air = self.path+'bj/airquality/bj_airquality_'+self.time_start+'-'+self.time_end+'.csv'
        self.path_bj_mete = self.path+'bj/observed_meteorology/bj_observed_mete_'+self.time_start+'-'+self.time_end+'.csv'
        self.path_bj_grid = self.path+'bj/meteorology_grid/bj_meteorology_grid_'+self.time_start+'-'+self.time_end+'.csv'
        self.path_ld_air = self.path+'ld/airquality/ld_airquality_'+self.time_start+'-'+self.time_end+'.csv'
        self.path_ld_grid = self.path+'ld/meteorology_grid/ld_meteorology_grid_'+self.time_start+'-'+self.time_end+'.csv'

    
    def respones_data(self):  
        self.respones_bj_air = requests.get(self.url_bj_air)
        self.respones_bj_mete = requests.get(self.url_bj_mete)
        self.respones_bj_grid = requests.get(self.url_bj_grid)
        self.respones_ld_air = requests.get(self.url_ld_air)
        self.respones_ld_grid = requests.get(self.url_ld_grid)



    def get_data(self):
        self.respones_data()
        
        with open (self.path_bj_air,'w') as f:
            f.write(self.respones_bj_air.text)
            print("done")
            f.close()

        with open ( self.path_bj_mete,'w') as f:
            f.write(self.respones_bj_mete.text)
            print("done")
            f.close()

        with open (self.path_bj_grid,'w') as f:
            f.write(self.respones_bj_grid.text)
            print("done")
            f.close()

        with open (self.path_ld_air,'w') as f:
            f.write(self.respones_ld_air.text)
            print("done")
            f.close()

        with open ( self.path_ld_grid,'w') as f:
            f.write(self.respones_ld_grid.text)
            print("done")
            f.close()


    

