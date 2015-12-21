app.controller('JPlayerCtrl', function($scope, $rootScope, PlaybackService) {
    $scope.isMute = false;
    $scope.isPlaying = false;
    $scope.isShuffle = false;
    $scope.isRepeat = false;
    $rootScope.volume = 1;

    PlaybackService.setBackend('PlaybackServiceJPlayer');
    $scope.playback = PlaybackService;

    $scope.$on('PLAY_TRACK', function(event, currentPlaylist, track){
        $scope.currentPlayTrack = track;
        if(track.type == 0){ //file
            PlaybackService.setTrack(track);
            PlaybackService.play();
        } else {
            console.error('Cannot play track of type '+track.type);
        }
    });

    $scope.$on('JUMP_TO_UNIT', function(event, unit){
        PlaybackService.seek(PlaybackService.totalTime() * unit);
    });

    $scope.$on('VOLUME_TO_UNIT', function(event, unit){
        $rootScope.volume = unit;
        $scope.playback.volume($rootScope.volume);
    });

    $rootScope.$on('DELETE_CURRENT_TRACK', function(event){
        $scope.currentPlayTrack = null;
    });

    $scope.mute = function(){
        $scope.playback.mute();
        $scope.isMute = true;
    };

    $scope.unmute = function(){
        $scope.playback.unmute();
        $scope.isMute = false;
    };

    $scope.maxVolume = function(){
        $rootScope.volume = 1;
        $scope.playback.volume($rootScope.volume);
    }

    $scope.currentPlaybackPercentage = 0;
    $rootScope.$on('PLAYBACK_TIME_UPDATE', function(event, currentTime, totalTime){
        $scope.currentPlayTime = currentTime;
        // PlaybackService gives correct totalTime always from metada, totalTime comes from JPlayer and sometimes fail
        $scope.currentPlaybackPercentage = currentTime / PlaybackService.totalTime() * 100;
        if(!$scope.$$phase) {
            $scope.$digest(); // HACK: force progress bar update
        }
    });
    $rootScope.$on('PLAYBACK_ENDED', function(event, currentTime, totalTime){
        $rootScope.isPlaying = true;

        console.log(currentTime);
        console.log(totalTime);
    });

});