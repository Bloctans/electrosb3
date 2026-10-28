uniform float brightness;

vec4 effect(vec4 color, Image texture, vec2 texture_coords, vec2 pixel_coords) {
    vec4 imageColor = Texel(texture, texture_coords);

    vec4 brightness_color = vec4(brightness,brightness,brightness,0);
    imageColor = clamp(imageColor + brightness_color, vec4(0), vec4(1));

    return imageColor * color;
}