
$(document).ready(function() {
    function updateScores() {
        $.ajax({
            url: "/get_live_scores",
            type: "GET",
            success: function(data) {
                // Update the scores on the page
                $("#home-score").text(data.home_score);
                $("#away-score").text(data.away_score);
                $("#time-clock").text(data.time_clock);
                $("#game-status").text(data.game_status);

                // Stop updating if the game is finished
                if (data.game_status === "STATUS_FINAL") {
                    clearInterval(scoreInterval);
                }
            }
        });
    }

    // Call the updateScores function initially
        setTimeout(function(){
            updateScores();

            var scoreInterval = setInterval(updateScores, 5000);
        }, 15000) //Todo fix interval or remove interval function is calling repeatedly and not waiting

    // Start updating the scores every 5 seconds
});
