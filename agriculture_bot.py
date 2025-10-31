# agriculture_bot.py
from agriculture_db import AgricultureDatabase

class AgricultureAIAssistant:
    def __init__(self):
        self.database = AgricultureDatabase()
        self.conversation_history = []
    
    def get_response(self, user_message):
        """Generate response using agriculture database"""
        
        # Analyze user question and get relevant data
        crop_info = self.extract_crop_info(user_message)
        response = ""
        
        if crop_info:
            # User asked about specific crop
            crop_name = crop_info['crop']
            crop_data = self.database.search_crop(crop_name)
            pest_data = self.database.search_pests(crop_name)
            fertilizer_data = self.database.search_fertilizer(crop_name)
            
            response = self.generate_crop_response(crop_name, crop_data, pest_data, fertilizer_data)
        else:
            # General agriculture question
            response = self.answer_general_question(user_message)
        
        # Add to conversation history
        self.conversation_history.append({"role": "user", "content": user_message})
        self.conversation_history.append({"role": "assistant", "content": response})
        
        return response
    
    def extract_crop_info(self, text):
        """Extract crop names from user text"""
        text_lower = text.lower()
        all_crops = self.database.get_all_crops()
        
        for crop in all_crops:
            if crop.lower() in text_lower:
                return {'crop': crop}
        return None
    
    def generate_crop_response(self, crop_name, crop_data, pest_data, fertilizer_data):
        """Generate detailed response about a specific crop"""
        response = f"🌱 **{crop_name.upper()} Farming Information**\n\n"
        
        if crop_data:
            response += f"**Growing Season:** {crop_data.get('season', 'N/A')}\n"
            response += f"**Soil Type:** {crop_data.get('soil_type', 'N/A')}\n"
            response += f"**Water Needs:** {crop_data.get('water_requirements', 'N/A')}\n"
            response += f"**Harvest Time:** {crop_data.get('harvest_time', 'N/A')}\n\n"
        else:
            response += "*Basic growing information not available in database*\n\n"
        
        if pest_data:
            response += "**Common Pests & Diseases:**\n"
            for pest in pest_data:
                response += f"• **{pest['pest_disease']}**: {pest['symptoms']}\n"
                response += f"  Organic Control: {pest['organic_control']}\n"
                response += f"  Chemical Control: {pest['chemical_control']}\n\n"
        else:
            response += "*Pest data not available for this crop*\n\n"
        
        if fertilizer_data:
            response += "**Fertilizer Recommendations:**\n"
            response += f"• NPK Ratio: {fertilizer_data.get('npk_ratio', 'N/A')}\n"
            response += f"• Organic Options: {fertilizer_data.get('organic_options', 'N/A')}\n"
            response += f"• Application Timing: {fertilizer_data.get('application_time', 'N/A')}\n"
        
        response += "\n💡 *Note: Local conditions may vary. Consult agricultural experts in your area.*"
        return response
    
    def answer_general_question(self, question):
        """Answer general agriculture questions"""
        question_lower = question.lower()
        
        if any(word in question_lower for word in ['hello', 'hi', 'hey']):
            return "🌾 Hello! I'm your Agriculture AI Assistant. I can help with crop information, pest management, fertilizer recommendations, and farming techniques. What would you like to know?"
        
        elif any(word in question_lower for word in ['crop', 'crops', 'grow']):
            available_crops = self.database.get_all_crops()
            if available_crops:
                crops_list = ", ".join(available_crops)
                return f"**Available Crop Information:**\n{crops_list}\n\nAsk about any specific crop for detailed growing information!"
            else:
                return "I can provide information about various crops. Try asking about wheat, rice, corn, tomato, or other common crops."
        
        elif any(word in question_lower for word in ['organic', 'natural']):
            return "**Organic Farming Tips:**\n• Use compost and green manure\n• Practice crop rotation\n• Use neem oil for pest control\n• Implement companion planting\n• Maintain soil health with organic matter"
        
        elif any(word in question_lower for word in ['water', 'irrigation']):
            return "**Water Management:**\n• Drip irrigation saves water\n• Water early morning or late evening\n• Monitor soil moisture\n• Use mulch to retain moisture\n• Consider rainwater harvesting"
        
        else:
            return "I specialize in crop information, pest management, and farming techniques. Try asking about:\n• Specific crops (wheat, rice, tomato, etc.)\n• Pest or disease problems\n• Fertilizer recommendations\n• Organic farming methods\n• Irrigation techniques"

    def clear_history(self):
        self.conversation_history = []