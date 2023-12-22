import plotly.express as px
def export_for_story(fig, name):
    fig.write_html(file= f'story_plots/{name}.html', include_plotlyjs = 'cdn', full_html = False)