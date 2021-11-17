import discord, asyncio, datetime, pytz, time

client = discord.Client()

@client.event
async def on_ready(): 
  async def message(games):
    await client.wait_until_ready()
    while not client.is_closed():
        for g in games:
           await client.change_presence(status=discord.Status.dnd) 
           await asyncio.sleep(5) #상태메세지 바뀌는 초 {현재는 5초로 설정되어있습니다.}
  print("\n===================[ 아래의 정보로 로그인 중.... ]==========================")
  print(("""[ Login ]\n이름 : {} \nBot 아이디 : {}""").format(client.user, client.user.id))
  print("디스코드 봇 버전 : " + str(discord.__version__))
  print("===================[ 로그인 완료...! ]==========================")
  await message(['' + str(len(client.guilds)) + '개의 서버와 함께','Made by : 놀자방 관리자'])
@client.event
@client.event
async def on_message(message):
    if message.content.startswith (".공지"): # 명령어,공지사항 코드
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(908537683389874177) # 공지 올라갈 채널 아이디
            #embed = discord.Embed(title="**🔥  놀자방 공지사항 🔥**", description="공지사항이 등록되었습니다! 확인해주세요.\n━━━━━━━━━━━━━━━━━━━\n{}\n\n".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xf80909)
            #embed.set_footer(text="놀자방 공지사항 | 담당 관리자 : {}".format(message.author), icon_url="https://cdn.discordapp.com/avatars/908735202996650084/8f05d2f404f55662d9a64ee7affc3a45.png")
            #embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/908735202996650084/8f05d2f404f55662d9a64ee7affc3a45.png")
            #await channel.send (embed=embed)
            #time.sleep(0.5)
            #await message.channel.send("@everyone")
            #print(f"\n[ 공지사항 시스템 ] ㅣ 놀자방 서버에서 {message.author}({message.author.id})님이 공지사항을 작성하였습니다.\n공지 내용 : {notice}")
            await message.channel.send("{}, 놀자방 공지 봇은 11월 20일에 서비스 시작합니다!ㅣ Made by : 뮤라#7191".format(message.author.mention))

        if i is False:
            y = datetime.datetime.now().year
            m = datetime.datetime.now().month
            d = datetime.datetime.now().day
            h = datetime.datetime.now().hour
            min = datetime.datetime.now().minute
            await message.channel.send("{}, 해당 명령어를 사용할 수 없습니다! ㅣ [ 해당 메세지는 콘솔창으로 전송됩니다. ]".format(message.author.mention))
            print(f"\n[ 공지 작성 실패 ] {message.author}({message.author.id})님이 공지 작성을 시도 하였습니다. [실패 사유 : 권한 부족]\n작성 시도 일시 : {y}년 {m}월 {d}일 {h}시 {min}분")
  
    
      
    if message.content.startswith (".청소"): #청소 기능 코드
        i = (message.author.guild_permissions.administrator)

        if i is True:
            #amount = message.content[4:]
            #await message.channel.purge(limit=1)
            #await message.channel.purge(limit=int(amount))

            #y = datetime.datetime.now().year
            #m = datetime.datetime.now().month
            #d = datetime.datetime.now().day
            #h = datetime.datetime.now().hour
            #min = datetime.datetime.now().minute
            #se = datetime.datetime.now().second
            #embed = discord.Embed(title="메시지 삭제 알림", description="**```디스코드 채팅 {}개가 관리자님의 요청으로 삭제가 되었습니다.```**".format(amount), color=0xf80909)
            #embed.set_footer(text=f"삭제 일시 : {y}년 {m}월 {d}일 {h}시 {min}분 {se}초 ㅣ 시스템 사용자 : {message.author}", icon_url="https://cdn.discordapp.com/avatars/908735202996650084/8f05d2f404f55662d9a64ee7affc3a45.png")
            #await message.channel.send(embed=embed)
            #print(f"\n[ 채팅 청소 사용자 알림 ] {message.author} 관리자님께서 채팅을 청소하였습니다. ㅣ 삭제 갯수 : {amount}개")
            await message.channel.send("{}, 놀자방 공지 봇은 11월 20일에 서비스 시작합니다!ㅣ Made by : 뮤라#7191".format(message.author.mention))
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 해당 명령어를 사용할 수 없습니다! ㅣ Made by : 뮤라#7191".format(message.author.mention))
            print(f"\n[ 채팅 청소 기능 시도 ] {message.author}님이 채팅 삭제를 시도하였습니다!")

    if message.content == "!관리명령어":
        if message.author.guild_permissions.administrator:
            await message.delete()

            embed = discord.Embed(title='**디스코드 관리 명령어 모음**', description='분류 : 디스코드 관리자 전용\n============================\n\n', color=0x05ece9)
            embed.set_author(name='놀자방 디스코드 관리 명령어 시스템', icon_url='https://cdn.discordapp.com/avatars/908735202996650084/8f05d2f404f55662d9a64ee7affc3a45.png')
            embed.add_field(name='청소 명령어',value='!청소 갯수', inline=False)
            embed.add_field(name='공지 명령어',value='!공지 내용', inline=False)
            embed.set_footer(text=f'디스코드 관리자 전용 명령어 모음 ㅣ Made by : 뮤라#7191')

            await message.channel.send(embed=embed)

        else:
            await message.delete()
            await message.channel.send('{}, 해당 유저는 관리자 전용 명령어를 볼 권한이 없습니다!'.format(message.author.mention)
)


            

client.run('OTA4NzM1MjAyOTk2NjUwMDg0.YY6Dmw.PESq2KiMnqGAkjZlKbXhc2X5YeE')