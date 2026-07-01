import discord
from discord.ext import commands
import os

# TOKEN (für Render / Hosting empfohlen)
TOKEN = os.getenv("Token")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)
# -------------------------
# READY
# -------------------------
@bot.event
async def on_ready():
    print(f"Online als {bot.user}")

    # persistent views (WICHTIG für Buttons / Tickets / Verify)
    bot.add_view(VerifyView())
    bot.add_view(TicketPanelView())

    try:
        synced = await bot.tree.sync()
        print(f"Slash Commands synced: {len(synced)}")
    except Exception as e:
        print(e)

    # 🔥 TIKTOK LOOP START
    bot.loop.create_task(tiktok_loop(bot))
       # Invite Rewards

@bot.tree.command(name="invite_rewards", description="Sendet Invite Rewards")
async def invite_rewards(interaction: discord.Interaction):

    invite_channel = bot.get_channel(1521305700838539366)

    if invite_channel:
        await invite_channel.send(
            "**NEW INVITE REWARDS FOR NOW ON!**\n\n"

            "📢 **INVITE REWARDS INFO** 🎁\n\n"

            "Earn keys by inviting friends! Here's what you get:\n\n"

            "➡️ **15 Invites** ─ 🚀 **10 Wins (Any Game)**\n"
            "➡️ **30 Invites** ─ 🚀 **15 Wins (Any Game)**\n"
            "➡️ **70 Invites** ─ 🚀 **25 Wins (Any Game)**\n\n"

            "❌ No Alt Accounts. Real users only!\n\n"

            "📨 Start inviting and claim your rewards!\n"
            "🎫 Open a ticket when you hit a reward tier.\n\n"

            "**Use `/invites` to check your invites.**\n\n"

            "@everyone"
        )
    await interaction.response.send_message(
        "✅ Gesendet",
        ephemeral=True
        )
    # Shop

@bot.tree.command(name="shop", description="Sendet den Shop")
async def shop(interaction: discord.Interaction):
    shop_channel = bot.get_channel(1521306643827003513)

    if shop_channel:
        await shop_channel.send(
        
        
            "**🛒 REGULAR SHOP**\n\n"

            "**💳 Payment Methods**\n"
            "• Paysafecard (16-digit Code)\n"
            "• PayPal Friends & Family\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n\n"

            "**📱 TikTok**\n"
            "• 1k Followers — **5€**\n"
            "• 1k Likes — **1.5€**\n"
            "• 1k Shares — **1.5€**\n"
            "• 1k Saves — **1.5€**\n"
            "• 10 Custom Comments — **1.5€**\n"
            "• 100k Views — **1.5€**\n\n"
            "📦 Stock: **9 Available**\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n\n"

            "**🚀 Discord Server Boosts**\n"
            "• 14× 1 Month Boosts — **11€**\n"
            "• 14× 3 Month Boosts — **16€**\n\n"
            "📦 Stock: **15 Available**\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n\n"

            "**💬 Discord Services**\n"
            "• 1k Offline Members — **6€**\n"
            "• 1k Online Members — **8€**\n"
            "• 25 Chat Members — **9€**\n"
            "• 10 Voice Members — **5€**\n"
            "• 1k Emoji Reactions — **6€**\n"
            "• 500 Button Reactions — **5€**\n"
            "• 500 Poll Reactions — **5€**\n\n"
            "📦 Stock: **100 Available**\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n\n"

            "💸 You can buy Followers, Likes, Views, Comments and much more at cheap prices.\n\n"

            "🎫 Create a ticket in **#💵・normal-shop** to place your order.\n\n"

            "**Minimum Order: 2.50€**"
        )
    await interaction.response.send_message(
        "✅ Gesendet",
        ephemeral=True
        )
    # TOS

@bot.tree.command(name="tos", description="Sendet die TOS")
async def tos(interaction: discord.Interaction):
    
    tos_channel = bot.get_channel(1521307122925568140)
    

    if tos_channel:
        await tos_channel.send(
            "**📜 OFFICIAL TOS**\n\n"

            "⚠️ **READ THESE TERMS BEFORE BUYING!**\n"
            "📸 Screenshot them if you want.\n"
            "✅ By purchasing, you automatically accept these Terms of Service.\n\n"

            "• Be respectful.\n"
            "• No support via DMs.\n"
            "• No vouch = No warranty.\n"
            "• Tickets inactive for more than 48 hours will be deleted.\n"
            "• If a supplier scams us, there will be no replacement or refund.\n"
            "• If your product has a problem, open a ticket on the same day.\n"
            "• If an account is revoked or deleted after delivery, there will be no replacement or refund.\n"
            "• PayPal payments must be Friends & Family with NO NOTES.\n"
            "• If a supplier makes a purchased product unusable after delivery, there will be no replacement or refund.\n"
            "• Only open serious tickets. Do not waste our time.\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n\n"

            "**📄 TOS:** #unknown\n"
            "**🗞️ Vouches:** #🗞️・feedback-vouches\n"
            "**🎫 Tickets:** #💵・normal-shop\n\n"

            "By staying in this server and purchasing from us, you agree to all of the above."
        )

    await interaction.response.send_message(
        "✅ Gesendet",
        ephemeral=True
        )
# -------------------------
# PRICES
# -------------------------
@bot.tree.command(name="prices", description="Zeigt Boosting Preise")
async def prices(interaction: discord.Interaction):

    embed = discord.Embed(
        title="Boosting Prices",
        color=0x2B2D31
    )

    await interaction.response.send_message(
        "✅ Gesendet",
        ephemeral=True
        )



# -------------------------
# VOUCH
# -------------------------
@bot.tree.command(name="vouch", description="Vouch a user with reason")
async def vouch(interaction: discord.Interaction, user: discord.Member, reason: str):

    log_channel = bot.get_channel(1521309946489209012)

    if log_channel:
        await log_channel.send(
            f"⭐ **VOUCH**\n\n"
            f"👤 User: {user.mention}\n"
            f"📝 Reason: {reason}\n"
            f"📌 Vouched by: {interaction.user.mention}"
        )

    await interaction.response.send_message(
        f"✅ Vouch sent for {user.mention}",
        ephemeral=True
    )


# -------------------------
# VERIFY VIEW (BUTTON)
# -------------------------
class VerifyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Verify",
        style=discord.ButtonStyle.success,
        emoji="✅",
        custom_id="verify_button"
    )
    async def verify(self, interaction: discord.Interaction, button: discord.ui.Button):

        guild = interaction.guild
        member = interaction.user

        verified_role = guild.get_role(1521341113972031505)
        unverified_role = guild.get_role(1521341190761353287)

        if verified_role:
            await member.add_roles(verified_role)

        if unverified_role:
            await member.remove_roles(unverified_role)

        await interaction.response.send_message(
            "✅ You are now verified!",
            ephemeral=True
        )

# -------------------------
# SEND VERIFY MESSAGE
# -------------------------
@bot.tree.command(name="setupverify", description="Send verify button")
async def setupverify(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📜 Verify to enter the server",
        description="Click the button below to get access.",
        color=0x2B2D31
    )

    await interaction.channel.send(embed=embed, view=VerifyView())

    await interaction.response.send_message(
        "✅ Verify message sent!",
        ephemeral=True
    )
    
# =========================
# TICKET SYSTEM CONFIG
# =========================

TICKET_CATEGORY_ID = 1521338581300285552

SUPPORT_ROLES = [
    1521311554048495747,  # Support
    1521311755492393001,  # CO Owner
    1521311659921248266   # Owner
]

open_tickets = {}


# =========================
# TICKET PANEL VIEW
# =========================

class TicketPanelView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.select(
        placeholder="🎫 Wähle eine Kategorie",
        options=[
            discord.SelectOption(label="Purchase", emoji="💰"),
            discord.SelectOption(label="Support", emoji="❓"),
            discord.SelectOption(label="Partnership", emoji="🤝"),
            discord.SelectOption(label="Report User", emoji="🚨"),
        ],
        custom_id="ticket_select"
    )
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):

        user = interaction.user

        if user.id in open_tickets:
            return await interaction.response.send_message(
                "❌ Du hast bereits ein Ticket offen!",
                ephemeral=True
            )

        guild = interaction.guild
        category = guild.get_channel(TICKET_CATEGORY_ID)

        channel_name = f"{select.values[0].lower()}-{user.name}"

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            user: discord.PermissionOverwrite(view_channel=True, send_messages=True),
        }

        for role_id in SUPPORT_ROLES:
            role = guild.get_role(role_id)
            if role:
                overwrites[role] = discord.PermissionOverwrite(
                    view_channel=True,
                    send_messages=True
                )

        channel = await guild.create_text_channel(
            name=channel_name,
            category=category,
            overwrites=overwrites
        )

        open_tickets[user.id] = channel.id

        embed = discord.Embed(
            title="🎫 Ticket erstellt",
            description=f"Hey {user.mention}, beschreibe dein Problem!",
            color=0x2B2D31
        )

        await channel.send(embed=embed, view=TicketControlView())

        await interaction.response.send_message(
            f"✅ Ticket erstellt: {channel.mention}",
            ephemeral=True
        )


# =========================
# TICKET CONTROL PANEL
# =========================

class TicketControlView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="🔒 Close", style=discord.ButtonStyle.danger)
    async def close(self, interaction: discord.Interaction, button: discord.ui.Button):

        open_tickets.pop(interaction.user.id, None)

        await interaction.response.send_message("Ticket wird geschlossen...", ephemeral=True)
        await interaction.channel.delete()

    @discord.ui.button(label="🗑 Delete", style=discord.ButtonStyle.gray)
    async def delete(self, interaction: discord.Interaction, button: discord.ui.Button):

        open_tickets.pop(interaction.user.id, None)

        await interaction.response.send_message("Ticket wird gelöscht...", ephemeral=True)
        await interaction.channel.delete()


# =========================
# SETUP COMMAND
# =========================

@bot.tree.command(name="setuptickets", description="Sendet das Ticket Panel")
async def setuptickets(interaction: discord.Interaction):

    embed = discord.Embed(
        title="🎫 Support Tickets",
        description=(
            "Wähle eine Kategorie:\n\n"
            "💰 Purchase\n"
            "❓ Support\n"
            "🤝 Partnership\n"
            "🚨 Report User"
        ),
        color=0x2B2D31
    )

    await interaction.channel.send(embed=embed, view=TicketPanelView())

    await interaction.response.send_message(
        "✅ Ticket Panel gesendet!",
        ephemeral=True
    )

import aiohttp
import asyncio
import discord

TIKTOK_USER = "aqz.gg"
NOTIFY_CHANNEL_ID = 1521502816919879690

last_video = None


async def fetch_latest_tiktok():
    url = f"https://www.tiktok.com/@{TIKTOK_USER}"

    headers = {"User-Agent": "Mozilla/5.0"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as r:
            html = await r.text()

    return html


async def tiktok_loop(bot):
    global last_video

    await bot.wait_until_ready()
    channel = bot.get_channel(NOTIFY_CHANNEL_ID)

    while not bot.is_closed():
        try:
            data = await fetch_latest_tiktok()

            if data and data != last_video:
                last_video = data

                embed = discord.Embed(
                    title="🎬 Neues TikTok erkannt!",
                    description=f"@{TIKTOK_USER} hat ein neues Video hochgeladen!",
                    color=0x00BFFF
                )

                if channel:
                    await channel.send("@everyone", embed=embed)

        except Exception as e:
            print("TikTok error:", e)

        await asyncio.sleep(300)
bot.run(TOKEN)
