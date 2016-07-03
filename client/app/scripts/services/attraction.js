'use strict';

/**
 * @ngdoc service
 * @name clientApp.Attraction
 * @description
 * # Attraction
 * Service in the clientApp.
 */
angular.module('clientApp')
  .service('Attraction', function ($resource, API_END_POINT) {
    return $resource(API_END_POINT + '/attractions/:id', {}, {
      query: {
        method: 'GET',
        isArray: true,
        transformResponse: function(data) {
          var records = angular.fromJson(data);

          if (!records) {
            return [];
          }

          // TODO: return Array of images from server side
          // instead of String
          if (angular.isArray(records)) {
            records.map(function(record) {
              if (record.images && record.images !== '') {
                record.images = JSON.parse(record.images);
              }
              return record;
            });
            return records;
          } else {
            return records;
          }
        }
      },

      get: {
        method: 'GET',
        transformResponse: function(data) {
          var record = angular.fromJson(data);

          if (!record) {
            return {};
          }

          // TODO: return Array of images from server side
          // instead of String
          if (angular.isObject(record)) {
            if (record.images && record.images !== '') {
              record.images = JSON.parse(record.images);
            }
            return record;
          } else {
            return record;
          }
        }
      }
    });
  });
