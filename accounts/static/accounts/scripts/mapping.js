let p_arrray = [];
let b_array = [];
let r_array = [];
var geo;
let congeo;
let tanzania;
//let tz;
let road;
var selections = [];
let map;
let constid;
$(document).ready(function() {
    let consts = L.featureGroup();
    let winners = [];
    let fname;
    let lname;
    let votestotal;
    let thecount = 4; //parties
    function randombetween(min, max) {
        return Math.floor(Math.random() * (max - min + 1) + min);
    }
    // return  array of random votes
    function generate(max, thecount) {
        var r = [];
        var currsum = 0;
        for (var i = 0; i < thecount - 1; i++) {
            r[i] = randombetween(1, max - (thecount - i - 1) - currsum);
            currsum += r[i];
        }
        r[thecount - 1] = max - currsum;
        return r;
    }

    function checkBounds(marker) {
        if (L.latLngBounds(swCorner, neCorner).contains(marker)) {
            return true;
        } else {
            return false;
        }
    }

    let buildings = L.layerGroup();
    let roads = L.layerGroup();
    let tz = L.layerGroup();
    let rg = L.layerGroup();
    let ds = L.layerGroup();
    let con = L.layerGroup();
    let wd = L.layerGroup();
    let wd_const = L.layerGroup();
    var selection;
    var selectedLayer;

    var m;
    let votes = [];
    let con_array = {};
    let wd_array = {};
    let reg_array = {}

    // function to eliminate duplicates in an array 
    function uniq(a) {
        return Array.from(new Set(a));
    }

    function arrayRemove(arr, value) {

        return arr.filter(function(ele) {
            return ele != value;
        });

    }

    function getPolygonColor(winerarray) {
        var i;
        var v = 0;
        var color;
        for (i = 0; i < winerarray.length; i++) {
            var win = winerarray[i].split('#')

            if (parseInt(win[2]) > v) {
                v = parseInt(win[2]);
                color = win[3];
                //console.log (v+""+ color); 

            }
        }

        return color;
    }

    function indexOflargest(a) {
        return a.indexOf(Math.max.apply(Math, a));
    }
    //rearrange array     
    Array.prototype.move = function(from, to) {
        this.splice(to, 0, this.splice(from, 1)[0]);
    };

    function checkTicK(ind, t) {

        return ind === t ? "<span class=\"glyphicon glyphicon-check\" style=\"color:red\"></span>" : "";

    }





    let url = "http://10.10.6.107:8081/geoserver/bongo/wms";
    let constlayer = L.tileLayer.wms(url, {
        layers: 'bongo:regions'

    });

    
    let consconst = L.tileLayer.wms(url, {
        layers: 'bongo:constituents'

    });





    var mbAttr = 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        mbUrl = 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiZGF2aWRrYSIsImEiOiJjanh5bHp1cWYwYXMwM2Jtdmc4aW1pazBsIn0.EAfNj4ZRn1V5atLW75Cq8A';

    var osmUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var osmAttrib = 'Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors';
    let osm = new L.TileLayer(osmUrl, {
        attribution: osmAttrib
    });

    let grayscale = L.tileLayer(mbUrl, {
            id: 'mapbox.light',
            attribution: mbAttr
        }),
        streets = L.tileLayer(mbUrl, {
            id: 'mapbox.streets',
            attribution: mbAttr
        });

    map = L.map('map', {
        center: [-6.78, 34.87],
        zoom: 6,

        layers: [constlayer, rg, con],
        fullscreenControl: true,
        fullscreenControlOptions: {
            position: "topleft", // optional
            title: "Show me fullscreen  Map!",
            titleCancel: "Exit fullscreen mode"

        }

    });

    let baseMaps = {
        "Grayscale": grayscale,
        "Streets": streets
            //'OSM': osm

    };

    var highlight = {
        'color': '#149c14',
        'weight': 4,
        'opacity': 1
    };

    
    //Regions
    $("#con").hide();
    $("#wd").hide();

    function zoomToFeature(e) {
        map.fitBounds(e.target.getBounds());
    }

    function hideLayers(D) {
        D.eachLayer(function(layer) {
            if (!layer.feature.properties.highlight) {
                map.removeLayer(layer);
            }
        });
    }

    function showLayers(D) {
        D.eachLayer(function(layer) {
            layer.feature.properties.highlight = false;
            map.addLayer(layer);
        });
    }
    $.getJSON('../get_regional_votes_geo', function(data) {
        rg.clearLayers();
        $("#selectregion option").remove();
        $("#selectregion").append("<option value=\"0\"> --Select-- </option>");
        var geojson = L.geoJson(data, {
            onEachFeature: function(feature, layer) {
                reg_array[parseInt(feature.properties.regionid)] = layer;
                rg.addLayer(layer);
                $("#selectregion").append("<option value=\'" + feature.properties.regionid + "\'>" + feature.properties.region_nam + "</ option>");
                layer.on('mouseover', function(e) {
                //     this.setStyle({
                //         opacity: 0.4,
                //         fillOpacity: 0.4
                //     });
                    layer.bindPopup("<h6>" + feature.properties.region_nam + "<br>" + "Votes:" + feature.properties.votes + "</h6>");
                    this.openPopup();

                });
                // layer.on('mouseout', function(e) {
                //     this.setStyle({
                //         opacity: 0.4,
                //         fillOpacity: 0.4 // back to original
                //     });

                //     this.closePopup();

                // });
                map.on('click', function(e) {
                    //having trouble with resetStyle, so just change it back
                    layer.setStyle({
                        'color': 'gray',
                        'weight': 3,
                        'opacity': 1
                    });
                    showLayers(geojson);
                });

                layer.on('click', function(e) {
                    this.setStyle(highlight);
                    e.target.feature.properties.highlight = true;
                    hideLayers(geojson);
                    zoomToFeature(e);

                    $("#selectregion").val(feature.properties.regionid);
                    map.fitBounds(e.target.getBounds());
                    // load constituencies
                    var region = feature.properties.region_nam;
                    $("#regname").text(region);
                    $.getJSON('../get_R_constituency_View/?region=' + region, function(datad) {
                        con.clearLayers();
                        $("#con").show();

                        $("#selectconstituent option").remove();
                        $("#selectconstituent").append("<option value=\"0\"> --Select-- </option>");
                        var geojson = L.geoJson(datad, {
                            style: function(feature) {
                                return {
                                    'color': 'brown',
                                    'weight': 4,
                                    'opacity': 0.5
                                };

                            },
                            onEachFeature: function(feature, layer) {

                                //populate list
                                $("#selectconstituent").append("<option value=\'" + feature.properties.constid + "\'>" + feature.properties.const+"</ option>");

                                con.addLayer(layer);
                                con_array[parseInt(feature.properties.constid)] = layer;
                                var divcont1 = "<table class=\"table\"> <thead><tr><th scope=\"col\">Name</th><th scope=\"col\">Votes</th>" +
                                    "</tr> </thead><tbody>";

                                layer.on('mouseover', function(e) {
                                    this.setStyle({
                                        //  'color': chamascolor[parseInt(feature.properties.chama_id) -1],
                                        // 'fillColor':chamascolor[parseInt(feature.properties.chama_id) -1],
                                        // opacity: 0.1,fillOpacity:0.1

                                    });
                                    layer.bindPopup("<h6>" + feature.properties.const+"</h6>");
                                    this.openPopup();

                                });
                                layer.on('mouseout', function(e) {
                                    this.setStyle({
                                        // color:'gray',
                                        // opacity: 0.1,fillOpacity:0.1// back to original
                                    });

                                    // this.closePopup();

                                });

                                map.on('click', function(e) {
                                    //having trouble with resetStyle, so just change it back
                                    //  layer.setStyle({
                                    //   'color': chamascolor[parseInt(feature.properties.chama_id) -1],
                                    //    'fillColor':chamascolor[parseInt(feature.properties.chama_id) -1],
                                    //   'weight': 3,
                                    //   'opacity': 1
                                    // });
                                    showLayers(geojson);
                                });

                                layer.on('click', function(e) {

                                    this.setStyle({
                                        'color': chamascolor[parseInt(feature.properties.chama_id) - 1],
                                        'fillColor': chamascolor[parseInt(feature.properties.chama_id) - 1],
                                        'weight': 3,
                                        'opacity': 1
                                    });

                                    //add pop up
                                    var wintable = "<table class=\"table\">  <thead>   <tr>" + "<th scope=\"col\"><span class=\"glyphicon glyphicon-check\"></th>" +
                                        "<th scope=\"col\"></th>   </tr> </thead> <tbody>";

                                    e.target.feature.properties.highlight = true;
                                    hideLayers(geojson);
                                    // zoomToFeature(e);

                                    $("#resultsdiv").empty();
                                    var constituency = layer.feature.properties.const;
                                    var const_id = layer.feature.properties.constid;
                                    $("#selectconstituent").val(feature.properties.constid);
                                    map.fitBounds(e.target.getBounds());
                                    $("#regname").text(region + " > " + constituency);
                                    $("#resultsdiv").empty();
                                    selections.length = 0;

                                    var convotes = [];

                                    $.getJSON("../PresVotesConst/?const=" + const_id, function(data) {

                                        wintable += "<tr><th scope=\"row\">Name</th> <td>" + data[0].fields.cand_name + "</td>"

                                + "</tr> <tr><th scope=\"row\">Votes</th>   <td>" + layer.feature.properties.votes + "</td>  </tr>" + "</tr> <tr><th scope=\"row\">Const</th>   <td>" + layer.feature.properties.const+"</td>  </tr>"

                                + " <tr> <th scope=\"row\">Party</th> <td>" + chamas[parseInt(layer.feature.properties.chama_id) - 1] + "</td> </tr>"

                                        $("#resultsdiv").empty();
                                        var st = "vertical-align: middle;  width: 40px;  height: 40px;  border-radius: 50%;";
                                        for (var i = 0; i < data.length; i++) {

                                            convotes.push(parseInt(data[i].fields.votes));

                                            divcont1 += "<tr><th scope=\"row\">" + (i + 1) + "</th>" +
                                                

                                                "<td>" + data[i].fields.cand_name + "</td>" +
                                                "<td>" + data[i].fields.votes + "</td></tr>";

                                        }
                                        divcont1 += "<tr><th scope=\"row\">Total</th>" +
                                            "<td></td><td></td><td></td><td>" + convotes.reduce((a, b) => a + b, 0) + "</td></tr></tbody> </table>";

                                        wintable += " </tbody></table>";
                                        $("#resultsdiv").html(divcont1);
                                        layer.bindPopup(wintable);
                                    });

                                    //layer.bindPopup(divcont);

                                    // load wards

                                    $.getJSON('../get_C_wards_View/?const=' + constituency, function(datac) {
                                        wd.clearLayers();
                                        $("#wd").show();

                                        $("#selectwards option").remove();
                                        $("#selectwards").append("<option value=\"0\"> --Select-- </option>");
                                        var geojson = L.geoJson(datac, {
                                            style: function(feature) {
                                                return {
                                                    color: '#8c8c8c',
                                                    opacity: 0.4,

                                                    fillOpacity: 0.4
                                                };

                                            },
                                            onEachFeature: function(feature, layer) {
                                                wd.addLayer(layer);
                                                wd_array[parseInt(feature.properties.wardid)] = layer;
                                                // populate wards select
                                                $("#selectwards").append("<option value=\'" + feature.properties.wardid + "\'>" + feature.properties.ward_name + "</ option>");

                                                layer.bindPopup("<p>" + feature.properties.ward_name + "<br>" + feature.properties.const+"<br>" + feature.properties.district_n + "<br>" + feature.properties.pk + "</p>");

                                                layer.on('mouseover', function(e) {
                                                    this.setStyle({
                                                        opacity: 0.2,
                                                        fillOpacity: 0.2
                                                    });
                                                    layer.bindPopup("<h6>" + feature.properties.ward_name + "</h6>");
                                                    this.openPopup();

                                                });
                                                layer.on('mouseout', function(e) {
                                                    this.setStyle({
                                                        opacity: 0.4,
                                                        fillOpacity: 0.4 // back to original
                                                    });

                                                    this.closePopup();

                                                });

                                                map.on('click', function(e) {
                                                    //having trouble with resetStyle, so just change it back
                                                    layer.setStyle({
                                                        'color': 'gray',
                                                        'weight': 3,
                                                        'opacity': 1
                                                    });
                                                    showLayers(geojson);
                                                });

                                                layer.on('click', function(e) {

                                                    this.setStyle({
                                                        color: '#8c8c8c',
                                                        opacity: 0.4,
                                                        fillColor: chamascolor[parseInt(feature.properties.chama_id) - 1],
                                                        fillOpacity: 0.4
                                                    });

                                                    e.target.feature.properties.highlight = true;
                                                    hideLayers(geojson);
                                                    zoomToFeature(e);

                                                    $("#resultsdiv").empty();
                                                    //map.setView(e.latlng, 8);
                                                    $("#selectwards").val(feature.properties.wardid);
                                                    map.fitBounds(e.target.getBounds());
                                                    $("#regname").text("Clicked: " + region + " > " + constituency + " > " + feature.properties.ward_name);

                                                    selections.length = 0;
                                                    var ward_id = feature.properties.wardid;

                                                    var wardvotes = [];

                                                    $.getJSON("../get_C_wards_Winners/?ward=" + ward_id, function(data) {
                                                        var st = "vertical-align: middle;  width: 40px;  height: 40px;  border-radius: 50%;";
                                                        var divcont2 = "<table class=\"table\"> <thead><tr> <th scope=\"col\">#</th>" +
                                                            "<th scope=\"col\">Symbol</th><th scope=\"col\">Photo</th><th scope=\"col\">Name</th><th scope=\"col\">Votes</th>" +
                                                            "</tr> </thead><tbody>";
                                                        $("#resultsdiv").empty();
                                                        for (var i = 0; i < data.length; i++) {

                                                            wardvotes.push(parseInt(data[i].fields.votes));

                                                            divcont2 += "<tr><th scope=\"row\">" + (i + 1) + "</th>" +
                                                                "<td><div class=\"" + "sm_" + chamascolor[parseInt(data[i].fields.chama_id) - 1] + "circle\"" + "></div></td>" +
                                                                "<td><img src=\"../../static/home/images/" + (i + 1) + ".png\"  alt=\"Avatar\"style=\"" + st + "\" class=\"avatar\"></td>" +
                                                                "<td>" + data[i].fields.candidate + "</td>" +
                                                                "<td>" + data[i].fields.votes + "</td></tr>";

                                                        }

                                                        divcont2 += "<tr><th scope=\"row\">Total</th>" + "<td></td><td></td><td></td><td>" + wardvotes.reduce((a, b) => a + b, 0) + "</td></tr></tbody> </table>";

                                                        $("#resultsdiv").html(divcont2);

                                                    });

                                                });

                                            }
                                        });

                                    }); //load wards

                                }); //click constituency

                            }
                        });

                    });

                }); //click regions
            }

        });

    });





//TZ
    $.getJSON('../get_regional_votes_geo', function(data) {

        var geojson = L.geoJson(data, {
            style: {
                // "color": "#FFFFFF",
                "weight": 5,
                "fillOpacity": 0.07,
                "opacity": 0.2
            },
            onEachFeature: function(feature, layer) {
                tz.addLayer(layer);
                // map.fitBounds(layer.getBounds()); // fit to country layer!
            }
        });

    });





    let overlayMaps = {
        "Region Names": constlayer,
        "Regions": rg,
        "Constituency": con,
        "Const Names": consconst,
       
        
    };
    L.control.layers(null, overlayMaps).addTo(map); //hide base map

    // handle onchange
    $('#errordiv').hide();
    //constituency
    $('select#selectconstituent').change(function() {
        var optionSelected = $(this).find("option:selected");

        var const_id = parseInt(optionSelected.val(), 10);

        if (const_id === 0) {
            $('#errordiv').html("<p>Invalid Selection</p>");
            $('#errordiv').show();
        } else {
            $('#errordiv').empty();
            // map.setView(con_array[const_id].getLatLng(), map.getZoom());
            map.fitBounds(con_array[const_id].getBounds());
        }

    });
    //wards

    $('select#selectwards').change(function() {
        var optionSelected = $(this).find("option:selected");
        var ward_id = parseInt(optionSelected.val(), 10);

        if (ward_id === 0) {

            $('#errordiv').html("<p>Invalid Selection</p>");
            $('#errordiv').show();
        } else {
            $('#errordiv').empty();
            map.fitBounds(wd_array[ward_id].getBounds());
        }

    });
    //region
    $('select#selectregion').change(function() {
        var optionSelected = $(this).find("option:selected");
        var reg_id = parseInt(optionSelected.val(), 10);

        if (reg_id === 0) {

            $('#errordiv').html("<p>Invalid Selection</p>");
            $('#errordiv').show();

        } else { //alert("region "+reg_id);
            //map.setView(reg_array[reg_id].getLatLng(), map.getZoom());
            $('#errordiv').empty();
            map.fitBounds(reg_array[reg_id].getBounds());
        }

    }); //onchange

}); //doc ready