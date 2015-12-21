app.controller('MainViewController', function($scope, $rootScope, $uibModal, $controller, PlaybackService, Playlist, Browse, IndexDirectory, track, djangoAuth){
    djangoAuth.authenticationStatus();

    angular.extend(this, $controller('HotkeysCtrl', {$scope: $scope}));
    $scope.openAboutModal = function(){
        var uibModalInstance = $uibModal.open({
            animation: true,
            templateUrl: STATIC_FILES + 'client/modals/about.html',
            controller: function($scope, $uibModalInstance){
                $scope.close = function(){
                    $uibModalInstance.dismiss('cancel');
                }
            }
        });
    };

    $scope.openChangePasswordModal = function(){
        var uibModalInstance = $uibModal.open({
            animation: true,
            templateUrl: STATIC_FILES + 'client/modals/change_password.html',
            scope: $scope,
            controller: function($scope, $uibModalInstance){
                $scope.close = function(){
                    $uibModalInstance.dismiss('cancel');
                }
            }
        });
    };

    PlaybackService.setBackend('PlaybackServiceJPlayer');
    $scope.playback = PlaybackService;

    $scope.userMayDownload = true;

    $scope.getRemainingTimeOrTracks = function (playlist) {
        return playlist.tracks.length;
    };
    $scope.getTotalTimeOrTracks = function (playlist) {
        return playlist.tracks.length;
    };

    $scope.getRemaingingPercentage = function (playlist) {
        return $scope.getRemainingTimeOrTracks(playlist) / $scope.getTotalTimeOrTracks(playlist) * 100
    };

    var createEmptyPlaylist = function(name, type){
        return {tracks: [], name: name, type: type};
    };

    var defaultPlaylist = createEmptyPlaylist('Queue', 'queue')
    $scope.playlists = [];
    $scope.openedPlaylists = [defaultPlaylist];
    $scope.currentPlaylist = defaultPlaylist;
    $scope.mediaBrowserMode = 'motd';

    $scope.$on('LOAD_PLAYLIST', function(event, playlist) {
        playlistid = playlist.id;
        var alreadyLoadedPlaylist = _.find(
            $scope.openedPlaylists,
            function(playlist){ return playlist.id == playlistid }
        );
        if(alreadyLoadedPlaylist){
            $scope.currentPlaylist = alreadyLoadedPlaylist;
        } else {
            playlist.loading = true;
            $scope.openedPlaylists.push(playlist);
            $scope.currentPlaylist = playlist;
            Playlist.get({id: playlistid}, function(playlist_data){
                playlist.loading = false;
                playlist.tracks = playlist_data.tracks;
            });
        }
    });

    $scope.fileBrowserContent = {};

    $scope.browse = function(directory){
        Browse.get(directory, function(data){
            $scope.fileBrowserContent = data
        });
        $scope.mediaBrowserMode = 'file'
    };

    $scope.$on('ADD_FILE_TO_PLAYLIST', function(event, file){
        $scope.currentPlaylist.tracks.push(track.fromFile(file));
    });

    $scope.$on('INDEX_DIRECTORY', function(event, path){
        IndexDirectory.index(path);
    });

    $scope.$on('LOAD_DIRECTORY', function(event, directory){
       $scope.browse(directory);
    });

    $scope.$on('PLAY_TRACK', function(event, currentPlaylist, track){
        $scope.currentPlayTrack = track
        if(track.type == 0){ //file
            PlaybackService.setTrack(track);
            PlaybackService.play();
        } else {
            console.error('Cannot play track of type '+track.type);
        }
    });

    $scope.showPlaylists = function(){
        $scope.mediaBrowserMode = 'playlist';
        Playlist.query(function(playlists){
            $scope.playlists = playlists;
        })
    };

    $scope.albumArtUrl = function(filepath){
        return API_URL + 'albumart/' + filepath
    };

    $scope.$on('CREATE_NEW_PLAYLIST', function(event){
        var newPlaylist = createEmptyPlaylist('New Playlist', 'playlist');
        $scope.openedPlaylists.push(newPlaylist);
        $scope.currentPlaylist = newPlaylist;
    });

    $scope.$on('JUMP_TO_UNIT', function(event, unit){
        console.log(unit)
        PlaybackService.seek(PlaybackService.totalTime() * unit);
    });

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
        console.log(currentTime);
        console.log(totalTime);
    });
});