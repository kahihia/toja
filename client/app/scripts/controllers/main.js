'use strict';

/**
 * @ngdoc function
 * @name clientApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the clientApp
 */
angular.module('clientApp')
.config(function($stateProvider) {

  $stateProvider
  .state('main', {
    url: '/',
    templateUrl: 'views/main.html',
    controller: 'MainCtrl as ctrl',
    resolve: {
      venues: function(Venue) {
        return Venue.query();
      }
    }
  });

})
.controller('MainCtrl', function () {
  this.venues = [
    {
      id: 94763,
      name: 'Sakuraya',
      address: 'Etoile Yoshihama 1F, 1-9, Yoshihamacho, Naka-ku, Yokohama-shi, Kanagawa, 231-0024',
      latitude: '35.436733',
      longitude: '139.645433',
      images: ['https://uds.gnst.jp/rest/img/mkej3x2b0000/s_00n2.jpg'],
      description: 'A large scale, Japanese-style show restaurant. <BR>Geisha, Samurai, Courtesans, and Kimono via modern Japanese entertainment is here!!'
    },
    {
      id: 94763,
      name: 'Sakuraya',
      address: 'Etoile Yoshihama 1F, 1-9, Yoshihamacho, Naka-ku, Yokohama-shi, Kanagawa, 231-0024',
      latitude: '35.436733',
      longitude: '139.645433',
      images: ['https://uds.gnst.jp/rest/img/mkej3x2b0000/s_00n2.jpg'],
      description: 'A large scale, Japanese-style show restaurant. <BR>Geisha, Samurai, Courtesans, and Kimono via modern Japanese entertainment is here!!'
    },
    {
      id: 94763,
      name: 'Sakuraya',
      address: 'Etoile Yoshihama 1F, 1-9, Yoshihamacho, Naka-ku, Yokohama-shi, Kanagawa, 231-0024',
      latitude: '35.436733',
      longitude: '139.645433',
      images: ['https://uds.gnst.jp/rest/img/mkej3x2b0000/s_00n2.jpg'],
      description: 'A large scale, Japanese-style show restaurant. <BR>Geisha, Samurai, Courtesans, and Kimono via modern Japanese entertainment is here!!'
    },
    {
      id: 94763,
      name: 'Sakuraya',
      address: 'Etoile Yoshihama 1F, 1-9, Yoshihamacho, Naka-ku, Yokohama-shi, Kanagawa, 231-0024',
      latitude: '35.436733',
      longitude: '139.645433',
      images: ['https://uds.gnst.jp/rest/img/mkej3x2b0000/s_00n2.jpg'],
      description: 'A large scale, Japanese-style show restaurant. <BR>Geisha, Samurai, Courtesans, and Kimono via modern Japanese entertainment is here!!'
    },
    {
      id: 94763,
      name: 'Sakuraya',
      address: 'Etoile Yoshihama 1F, 1-9, Yoshihamacho, Naka-ku, Yokohama-shi, Kanagawa, 231-0024',
      latitude: '35.436733',
      longitude: '139.645433',
      images: ['https://uds.gnst.jp/rest/img/mkej3x2b0000/s_00n2.jpg'],
      description: 'A large scale, Japanese-style show restaurant. <BR>Geisha, Samurai, Courtesans, and Kimono via modern Japanese entertainment is here!!'
    }
  ];
});
