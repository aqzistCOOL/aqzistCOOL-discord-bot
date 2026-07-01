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

    bot.add_view(VerifyView())

    try:
        synced = await bot.tree.sync()
        print(f"Slash Commands synced: {len(synced)}")
    except Exception as e:
        print(e)
@bot.event
async def on_member_join(member):
    role = member.guild.get_role(1521341190761353287)

    if role:
        await member.add_roles(role)
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
    


bot.run(TOKEN)
