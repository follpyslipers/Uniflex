{% load static %}

{% extends 'lecture/main-lecture.html' %}

{% block lecture %}

    <h1>Lectures</h1>


    <!-- Analyses -->
    {% if live_lectures_count > 0 %}
    {% for lecture in lectures %}
        <div class="analyse">
            <div class="sales">
                <div class="status">
                    <div class="info">
                        {% if lecture.status == 'Live' %}

                                {% with latest_live_lecture=lecture %}
                                    <h1>{{ latest_live_lecture.course.name }}</h1>
                                    <p>Date: {{ latest_live_lecture.date }}</p>
                                    <p>Start Time: {{ latest_live_lecture.start_time }}</p>
                                    <p>End Time: {{ latest_live_lecture.end_time }}</p>
                                    
                                {% endwith %}

                        {% endif %}
                    </div>
                </div>
            </div>
        </div>
    {% endfor %}
    {% else %}
    <p>No live lectures found.</p>
    {% endif %}

{% endblock lecture %}