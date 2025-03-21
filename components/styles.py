def load_css():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    
    .container {
        width: 100%;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }
    
    .profile-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .profile-image {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        object-fit: cover;
        margin-bottom: 1.5rem;
        border: 3px solid #f0f0f0;
    }
    
    .profile-name {
        font-size: 2rem;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 0.4rem;
    }
    
    .profile-title {
        font-size: 1.1rem;
        color: #666;
        margin-bottom: 1.5rem;
    }
    
    .tech-section {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        justify-content: center;
        margin: 2rem 0;
    }
    
    .tech-badge {
        height: 28px;
        opacity: 0.9;
        transition: opacity 0.2s;
    }
    
    .tech-badge:hover {
        opacity: 1;
    }
    
    .contact-section {
        border-top: 1px solid #eee;
        padding-top: 1.5rem;
        margin-top: 1.5rem;
        display: flex;
        justify-content: center;
        gap: 12px;
    }
    
    .contact-button {
        padding: 8px 20px;
        border-radius: 6px;
        font-size: 0.95rem;
        text-decoration: none;
        color: #fff;
        background: #2a2a2a;
        transition: all 0.2s;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .contact-button:hover {
        background: #3b3b3b;
        transform: translateY(-1px);
    }

    /* ========== CHAT IMPROVEMENTS ========== */
    .chat-container {
        background: #ffffff;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        height: 600px;
        display: flex;
        flex-direction: column;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }

    .chat-messages {
        flex: 1;
        overflow-y: auto;
        padding: 1.5rem;
        display: flex;
        flex-direction: column;
        gap: 1.5rem;
        background: #f9fafb;
    }

    .message {
        max-width: 78%;
        padding: 16px 20px;
        border-radius: 20px;
        font-size: 0.95rem;
        line-height: 1.5;
        animation: fadeIn 0.3s ease;
        position: relative;
        transition: transform 0.2s;
    }

    .user-message {
        background: #2563eb;
        color: white;
        align-self: flex-end;
        margin-left: 22%;
        border-bottom-right-radius: 6px;
    }

    .bot-message {
        background: #ffffff;
        color: #1f2937;
        border: 1px solid #e5e7eb;
        align-self: flex-start;
        margin-right: 22%;
        border-bottom-left-radius: 6px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
    }

    .message-avatar {
        position: absolute;
        bottom: -10px;
        width: 32px;
        height: 32px;
        border-radius: 6px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 14px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .user-message .message-avatar {
        right: -38px;
        background: #2563eb;
        color: white;
    }

    .bot-message .message-avatar {
        left: -38px;
        background: #fff;
        color: #6b7280;
        border: 1px solid #e5e7eb;
    }

    .chat-input-container {
        padding: 1.5rem;
        border-top: 1px solid #e5e7eb;
        background: #ffffff;
    }

    .chat-input-wrapper {
        position: relative;
        max-width: 800px;
        margin: 0 auto;
    }

    .chat-input {
        width: 100%;
        padding: 14px 52px 14px 20px;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        font-size: 1rem;
        transition: all 0.2s;
        background: #fff;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    }

    .chat-input:focus {
        outline: none;
        border-color: #2563eb;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
    }

    .send-button {
        position: absolute;
        right: 14px;
        top: 50%;
        transform: translateY(-50%);
        background: none;
        border: none;
        color: #2563eb;
        cursor: pointer;
        padding: 8px;
        border-radius: 8px;
        transition: all 0.2s;
    }

    .send-button:hover {
        background: #f3f4f6;
        transform: translateY(-50%) scale(1.05);
    }

    /* ========== CARD IMPROVEMENTS ========== */
    .project-card, .post-card {
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        background: white;
        cursor: pointer;
        box-shadow: 0 2px 4px rgba(0,0,0,0.03);
    }

    .project-card:hover, .post-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    }

    .card-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 1rem;
    }

    .card-icon {
        width: 44px;
        height: 44px;
        object-fit: contain;
        border-radius: 8px;
    }

    .card-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 4px;
    }

    .card-subtitle {
        color: #6b7280;
        font-size: 0.9rem;
    }

    .card-content {
        color: #4b5563;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 1rem;
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }

    .card-expanded .card-content {
        -webkit-line-clamp: unset;
    }

    .read-more {
        color: #2563eb;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 6px;
        transition: all 0.2s;
    }

    .read-more:hover {
        gap: 8px;
    }

    .tech-stack {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 1rem;
    }

    .tech-item {
        background: #f3f4f6;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        color: #4b5563;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .chat-messages::-webkit-scrollbar {
        width: 8px;
    }

    .chat-messages::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 4px;
    }

    .chat-messages::-webkit-scrollbar-thumb {
        background: #c1c1c1;
        border-radius: 4px;
    }
    </style>
    """