# download_agri_data.py
import pandas as pd
import os

def download_agriculture_data():
    """Create agriculture databases"""
    
    # Create data folder
    if not os.path.exists('agri_data'):
        os.makedirs('agri_data')
    
    print("🌱 Creating agriculture databases...")
    
    # Crop database
    crops_data = {
        'crop': ['Wheat', 'Rice', 'Corn', 'Soybean', 'Potato', 'Tomato', 'Cotton', 'Sugarcane'],
        'season': ['Rabi', 'Kharif', 'Kharif', 'Kharif', 'Rabi', 'All', 'Kharif', 'All'],
        'soil_type': ['Loamy', 'Clayey', 'Well-drained', 'Well-drained', 'Sandy loam', 'Well-drained', 'Black', 'Alluvial'],
        'water_requirements': ['Medium', 'High', 'Medium', 'Medium', 'Medium', 'High', 'Low', 'High'],
        'harvest_time': ['120-140 days', '150-180 days', '100-120 days', '100-120 days', '90-120 days', '70-90 days', '180-200 days', '300-365 days']
    }
    
    # Pest and disease database
    pests_data = {
        'crop': ['Wheat', 'Rice', 'Corn', 'Tomato', 'Cotton', 'Potato'],
        'pest_disease': ['Rust Fungus', 'Bacterial Blight', 'Corn Borer', 'Early Blight', 'Bollworm', 'Late Blight'],
        'symptoms': ['Orange pustules on leaves', 'Yellow streaks on leaves', 'Holes in stems', 'Dark spots on leaves', 'Holes in bolls', 'Brown spots on leaves'],
        'organic_control': ['Neem oil spray', 'Copper fungicide', 'Neem extract', 'Baking soda spray', 'Neem oil', 'Copper fungicide'],
        'chemical_control': ['Propiconazole', 'Streptomycin', 'Chlorpyrifos', 'Chlorothalonil', 'Cypermethrin', 'Mancozeb']
    }
    
    # Fertilizer recommendations
    fertilizer_data = {
        'crop': ['Wheat', 'Rice', 'Corn', 'Soybean', 'Potato', 'Tomato'],
        'npk_ratio': ['80:40:20', '100:50:50', '120:60:40', '20:80:40', '100:50:100', '80:40:60'],
        'organic_options': ['Compost + Vermicompost', 'Farmyard manure', 'Green manure', 'Rhizobium culture', 'Well-rotted manure', 'Compost tea'],
        'application_time': ['Before sowing + during tillering', 'Basal + tillering', 'Basal + knee-high stage', 'At sowing', 'At planting', 'Transplanting + flowering']
    }
    
    # Save to CSV files
    pd.DataFrame(crops_data).to_csv('agri_data/crops_database.csv', index=False)
    pd.DataFrame(pests_data).to_csv('agri_data/pests_database.csv', index=False) 
    pd.DataFrame(fertilizer_data).to_csv('agri_data/fertilizer_database.csv', index=False)
    
    print("✅ Agriculture databases created!")
    print("📁 Files saved in 'agri_data' folder:")
    print("   - crops_database.csv")
    print("   - pests_database.csv") 
    print("   - fertilizer_database.csv")

if __name__ == "__main__":
    download_agriculture_data()