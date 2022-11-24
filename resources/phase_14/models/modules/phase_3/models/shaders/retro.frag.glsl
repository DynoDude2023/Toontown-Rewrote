#version 330

#define PI 3.14159265f

uniform sampler2D p3d_Texture0;
in vec2 texcoord;
out vec4 o_color;

float ScanlineAmount = 0.65f;
float ScanlineScale = 1.0f;
float ScanlineBrightScale = 1.0f;
float ScanlineBrightOffset = 1.0f;
float ScanlineOffset = 0.0f;
float ScanlineHeight = 1.0f;
float RawWidth = 320;
float RawHeight = 224;

uniform vec2 sourceDims;

void main() {
    vec4 c0 = texture(p3d_Texture0, texcoord);
	int biasColor = int(texcoord * RawWidth * 3) % 3;
	c0[biasColor] *= 1.2;
	vec4 color = vec4(c0.r + (c0.g * 0.1) + (c0.b * 0.1), c0.g + (c0.r * 0.1) + (c0.b * 0.1), c0.b + (c0.g * 0.1) + (c0.r * 0.1), c0.a);

    float pixelRatio = RawHeight / sourceDims.y;

    vec2 BaseCoord = texcoord;

    vec2 ScanCoord = BaseCoord - 0.5f / sourceDims;
    //vec2 ScanCoord = BaseCoord;
    ScanCoord.y *= pixelRatio;

    float InnerSine = ScanCoord.y * RawHeight * ScanlineScale;
    float ScanBrightMod = sin(InnerSine * PI + ScanlineOffset * RawHeight);
    float ScanBrightness = mix(1.0f, (pow(ScanBrightMod * ScanBrightMod, ScanlineHeight) * ScanlineBrightScale + 1.0f) * 0.5f, ScanlineAmount);

    // output
    o_color = vec4(color.rgb * ScanBrightness, color.a);
}
