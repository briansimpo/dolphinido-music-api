from masonite.routes import Route

ROUTES = [

    Route.get("country_list", "api.common.UtilityController@country_list"),
    Route.get("year_list", "api.common.UtilityController@year_list"),

    Route.api("album_releases", "api.common.AlbumReleasesController"),
    Route.api("artist_types", "api.common.ArtistTypesController"),
    Route.api("genres", "api.common.GenresController"),


    Route.group([
        Route.get("user", "auth.AuthController@user"),
        Route.put("user/avatar", "api.user.UserImageController@update"),

    ], middleware=["guard:jwt"]),


    Route.group([
        Route.api("artist", "api.portal.ArtistController"),
        Route.api("albums", "api.portal.AlbumsController"),
        Route.api("songs", "api.portal.SongsController"),
        Route.api("shows", "api.portal.ShowsController"),

        Route.put("artist/avatar", "api.portal.ArtistImageController@update"),

        Route.put("albums/@id/publish", "api.portal.AlbumsController@publish"),
        Route.put("albums/@id/unpublish", "api.portal.AlbumsController@unpublish"),
        Route.put("songs/@id/publish", "api.portal.SongsController@publish"),
        Route.put("songs/@id/unpublish", "api.portal.SongsController@unpublish"),
        Route.get("unknown_album_songs", "api.portal.SongsController@unknown_album"),

        Route.put("shows/@id/publish", "api.portal.ShowsController@publish"),
        Route.put("shows/@id/unpublish", "api.portal.ShowsController@unpublish"),

        Route.put("albums/@id/cover_image", "api.portal.AlbumImageController@update"),
        Route.put("songs/@id/cover_image", "api.portal.SongImageController@update"),
        Route.put("shows/@id/cover_image", "api.portal.ShowImageController@update"),

        Route.post("albums/tracks", "api.portal.AlbumTracksController@store"),
        Route.delete("albums/tracks/@id", "api.portal.AlbumTracksController@delete"),

        Route.post("shows/performers", "api.portal.ShowPerformersController@store"),
        Route.delete("shows/performers/@id", "api.portal.ShowPerformersController@delete"),

    ], prefix="portal", middleware=["guard:jwt"]),

    Route.group([
        Route.api("artists", "api.discover.ArtistsController"),
        Route.api("albums", "api.discover.AlbumsController"),
        Route.api("album_downloads", "api.discover.AlbumDownloadsController"),
        Route.api("album_likes", "api.discover.AlbumLikesController"),
        Route.api("songs", "api.discover.SongsController"),
        Route.api("song_downloads", "api.discover.SongDownloadsController"),
        Route.api("song_likes", "api.discover.SongLikesController"),
        Route.api("song_plays", "api.discover.SongPlaysController"),
        Route.api("followings", "api.discover.FollowingsController"),
        Route.api("genres", "api.discover.GenresController"),
        Route.api("playlists", "api.discover.PlaylistsController"),

    ], prefix="discover", middleware=["guard:jwt"])
]
