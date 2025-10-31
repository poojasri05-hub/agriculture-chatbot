# agriculture_db.py
import pandas as pd
import os

class AgricultureDatabase:
    def __init__(self):
        self.data_folder = 'agri_data'
        self.load_databases()
    
    def load_databases(self):
        """Load all agriculture databases"""
        try:
            self.crops_df = pd.read_csv(f'{self.data_folder}/crops_database.csv')
            self.pests_df = pd.read_csv(f'{self.data_folder}/pests_database.csv')
            self.fertilizer_df = pd.read_csv(f'{self.data_folder}/fertilizer_database.csv')
            print("✅ Agriculture databases loaded successfully!")
        except FileNotFoundError:
            print("❌ Database files not found. Please run download_agri_data.py first")
            # Create empty dataframes to prevent errors
            self.crops_df = pd.DataFrame()
            self.pests_df = pd.DataFrame()
            self.fertilizer_df = pd.DataFrame()
    
    def search_crop(self, crop_name):
        """Search for crop information"""
        crop_name = crop_name.lower().strip()
        result = self.crops_df[self.crops_df['crop'].str.lower() == crop_name]
        if not result.empty:
            return result.iloc[0].to_dict()
        return None
    
    def search_pests(self, crop_name):
        """Search for pests and diseases of a crop"""
        crop_name = crop_name.lower().strip()
        results = self.pests_df[self.pests_df['crop'].str.lower() == crop_name]
        if not results.empty:
            return results.to_dict('records')
        return []
    
    def search_fertilizer(self, crop_name):
        """Search fertilizer recommendations for a crop"""
        crop_name = crop_name.lower().strip()
        result = self.fertilizer_df[self.fertilizer_df['crop'].str.lower() == crop_name]
        if not result.empty:
            return result.iloc[0].to_dict()
        return None
    
    def get_all_crops(self):
        """Get list of all available crops"""
        return self.crops_df['crop'].tolist() if not self.crops_df.empty else []