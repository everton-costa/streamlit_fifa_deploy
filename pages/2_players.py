import streamlit as st

df_data = st.session_state['data']

clubes = df_data['Club'].unique()
club = st.sidebar.selectbox('Clube', clubes)

df_club = df_data[df_data['Club'] == club].copy()
players = df_club.index.unique()
player = st.sidebar.selectbox('Jogador', players)

player_stats = df_data[df_data.index == player]

st.image(player_stats.Photo[0])
st.title(player_stats.index[0])
st.markdown(f'**Clube:** {player_stats.Club[0]}')
st.markdown(f'**Posição:** {player_stats.Position[0]}')
col1, col2, col3, col4, col5 = st.columns(5)
col1.markdown(f'**Idade:** {player_stats["Age"][0]}')
col2.markdown(f'**Altura:** {player_stats["Height(cm.)"][0]/100}m')
col3.markdown(f'**Peso:** {player_stats["Weight(lbs.)"][0]*0.453:.1f}kg')
col4.markdown(f'**Pé:** {player_stats["Preferred Foot"][0]}')

st.divider()

st.subheader(f'Overall {player_stats.Overall[0]}')
st.progress(int(player_stats.Overall[0]))
col1, col2, col3 = st.columns(3)
col1.metric(label='Valor de mercado', value=f'{player_stats["Value(£)"][0]:,}')
col2.metric(label='Salário semanal', value=f'{player_stats["Wage(£)"][0]:,}')
col3.metric(label='Cláusula de rescisão', value=f'{player_stats["Release Clause(£)"][0]:,}')
