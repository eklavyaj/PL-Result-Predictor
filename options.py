teams = ['Aston Villa', 'Barnsley', 'Birmingham City', 'Blackburn Rovers', 'Blackpool', 'Bolton Wanderers', 'Bournemouth', 'Bradford City', 'Brighton', 'Burnley', 'Cardiff City', 'Charlton Athletic', 'Chelsea', 'Coventry City', 'Crystal Palace', 'Derby County', 'Everton', 'Fulham', 'Huddersfield Town', 'Hull City', 'Ipswich Town', 'Leeds United', 'Leicester City', 'Liverpool', 'Manchester City', 'Manchester United', 'Middlesbrough', 'Newcastle United', 'Norwich City', 'Nottingham Forest', 'Portsmouth', 'Queens Park Rangers', 'Reading', 'Sheffield United', 'Sheffield Wednesday', 'Southampton', 'Stoke City', 'Sunderland', 'Swansea City', 'Tottenham Hotspur', 'Watford', 'West Bromwich Albion', 'West Ham United', 'Wigan', 'Wimbledon', 'Wolverhampton Wanderers'] 



with open("options.txt", "w") as f:

    for x in teams:
        line = "<option value = \"" +x +"\">"+ x+ "</option>\n"
        f.write(line)
