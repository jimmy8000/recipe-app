from io import BytesIO
import base64
import matplotlib.pyplot as plt

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10, 6))

    if chart_type == '#1':
        if 'difficulty' in data.columns:
            data['difficulty'].value_counts().plot(kind='bar')
            plt.xlabel('Difficulty Level')
            plt.ylabel('Number of Recipes')
            plt.title('Number of Recipes by Difficulty Level')
        else:
            print('Missing column: difficulty')
    elif chart_type == '#2':
        if 'difficulty' in data.columns:
            labels = kwargs.get('labels')
            plt.pie(data['difficulty'].value_counts(), labels=labels, autopct='%1.1f%%')
            plt.title('Recipe Distribution by Difficulty Level')
        else:
            print('Missing column: difficulty')
    elif chart_type == '#3':
        if 'cooking_time' in data.columns:
            data['cooking_time'].plot(kind='line')
            plt.xlabel('Recipe Index')
            plt.ylabel('Cooking Time (minutes)')
            plt.title('Cooking Time of Recipes')
        else:
            print('Missing column: cooking_time')
    else:
        print('Unknown chart type')

    plt.tight_layout()
    chart = get_graph()
    return chart