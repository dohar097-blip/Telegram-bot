from config.settings import PRODUCTS


class ProductManager:
    """Sonic Brand Market এর পণ্য ম্যানেজমেন্ট"""
    
    @staticmethod
    def get_all_products():
        """সকল পণ্য পান"""
        return PRODUCTS
    
    @staticmethod
    def get_product(product_id):
        """নির্দিষ্ট পণ্য পান"""
        return PRODUCTS.get(product_id)
    
    @staticmethod
    def format_product_catalog():
        """পণ্য ক্যাটালগ ফর্ম্যাট করুন"""
        catalog = "🛍️ **Sonic Brand Market - প্রোডাক্ট ক্যাটালগ**\n\n"
        
        for product_id, product in PRODUCTS.items():
            catalog += f"📦 **{product['name']}**\n"
            catalog += f"   💰 মূল্য: ৳{product['price']}\n"
            catalog += f"   📝 {product['description']}\n"
            catalog += f"   ✨ বৈশিষ্ট্য:\n"
            for feature in product['features']:
                catalog += f"      • {feature}\n"
            catalog += "\n"
        
        return catalog
    
    @staticmethod
    def get_product_info(product_id):
        """পণ্যের বিস্তারিত তথ্য"""
        product = PRODUCTS.get(product_id)
        if not product:
            return "❌ পণ্য পাওয়া যায়নি"
        
        info = f"📦 **{product['name']}**\n\n"
        info += f"💰 **মূল্য:** ৳{product['price']}\n"
        info += f"📝 **বর্ণনা:** {product['description']}\n\n"
        info += f"✨ **বৈশিষ্ট্য:**\n"
        for feature in product['features']:
            info += f"   • {feature}\n"
        
        return info
