import pandas as pd


df = pd.read_csv('/Users/chapmanlm/Downloads/db_test/JIMB_variants.csv')
df_original = pd.read_csv('/Users/chapmanlm/Downloads/db_test/original_db.csv')

matches = 'HG2_Ill_250bpfermikitraw_7557|HG2_Ill_Krunchall_11173|HG2_PB_SVrefine2PB10Xhap12_10658|HG4_Ill_scalpel_9189|HG2_Ill_FB_10417|HG2_Ill_150bpfermikitraw_13283|HG4_PB_HySA_1839|HG3_PB_HySA_22631|HG3_Ill_150bpfermikitraw_7748|HG4_Ill_FB_11028|HG2_PB_HySA_9922|HG4_Ill_GATKHCSBGrefine_12865|HG2_PB_assemblyticsfalcon_25146|HG4_Ill_scalpel_13834|HG4_Ill_svaba_5734|HG4_Ill_Krunchall_8666|HG3_Ill_250bpfermikitraw_7366|HG3_Ill_FB_830|HG3_Ill_FB_16613|HG2_CG_vcfBeta_7493|HG2_Ill_GATKHC_19359|HG2_Ill_scalpel_553|HG3_Ill_GATKHC_29197|HG4_Ill_scalpel_17320|HG4_PB_HySA_14912|HG3_Ill_GATKHC_2182|HG4_Ill_250bpfermikitraw_24923|HG3_Ill_Krunchall_21525|HG2_Ill_150bpfermikitraw_24627|HG3_Ill_svaba_10305|HG4_PB_assemblyticsfalcon_7114|HG3_Ill_Krunchall_19213|HG2_Ill_GATKHC_20719|HG4_Ill_svaba_5511|HG2_Ill_Krunchall_17274|HG4_Ill_Krunchall_10620|HG3_Ill_scalpel_6523|HG2_Ill_GATKHC_19838|HG2_PB_assemblyticsPBcR_14320|HG3_Ill_svaba_3557|HG3_Ill_FB_10579|HG4_Ill_FB_7787|HG3_Ill_250bpfermikitraw_19249|HG4_Ill_250bpfermikitraw_16428|HG2_Ill_GATKHC_9998|HG3_Ill_GATKHC_15837|HG3_PB_assemblyticsfalcon_547|HG2_Ill_Krunchall_277|HG3_Ill_Spiral_10643|HG3_Ill_Krunchall_1398|HG2_Ill_150bpfermikitraw_318|HG3_Ill_150bpfermikitraw_13622|HG4_CG_vcfBeta_11849|HG4_CG_vcfBeta_9145|HG4_Ill_svaba_2488|HG2_PB_assemblyticsfalcon_4138|HG4_Ill_Krunchall_11933|HG4_Ill_scalpel_4415|HG2_Ill_scalpel_14227|HG4_PB_HySA_17593|HG2_Ill_GATKHC_23326|HG3_PB_HySA_23831|HG3_PB_assemblyticsfalcon_13924|HG3_Ill_FB_820|HG3_Ill_150bpfermikitraw_8539|HG2_CG_vcfBeta_2914|HG3_Ill_scalpel_14498|HG2_Ill_GATKHC_16308|HG2_PB_assemblyticsfalcon_26785|HG4_Ill_svaba_20465|HG3_Ill_GATKHC_18727|HG4_CG_vcfBeta_9376|HG4_Ill_FB_13034|HG4_Ill_Cortex_3569|HG3_Ill_250bpfermikitraw_8989|HG4_CG_vcfBeta_6722|HG4_CG_vcfBeta_4103|HG2_CG_vcfBeta_433|HG2_Ill_SVrefine2DISCOVARplusDovetail_10810|HG3_PB_assemblyticsfalcon_7547|HG2_CG_vcfBeta_6703|HG2_PB_HySA_29753|HG3_Ill_scalpel_4399|HG4_Ill_250bpfermikitraw_9772|HG2_Ill_SpiralSDKrefine_361|HG4_Ill_Krunchall_10418|HG3_Ill_scalpel_8573|HG3_Ill_GATKHC_24907|HG2_Ill_GATKHC_7840|HG3_Ill_250bpfermikitraw_10235|HG2_PB_assemblyticsPBcR_8326|HG2_PB_assemblyticsPBcR_27417|HG3_Ill_svaba_12365|HG4_Ill_Krunchall_22535|HG2_Ill_SpiralSDKrefine_9399|HG2_PB_HySA_8916|HG3_Ill_GATKHC_17356|HG4_Ill_scalpel_6915|HG2_PB_HySA_19338|HG2_Ill_GATKHC_20719|HG4_Ill_GATKHC_17194|HG3_Ill_FB_10972|HG3_Ill_150bpfermikitraw_2864|HG4_Ill_Krunchall_22639|HG2_Ill_Krunchall_20062|HG2_Ill_250bpfermikitraw_9327|HG3_Ill_GATKHC_3005|HG3_Ill_GATKHC_11548|HG2_Ill_250bpfermikitraw_10402|HG3_Ill_svaba_5145|HG2_Ill_svaba_18702|HG2_Ill_FB_9640|HG3_Ill_Spiral_12891|HG3_Ill_Spiral_6945|HG4_PB_assemblyticsfalcon_22456|HG4_PB_assemblyticsfalcon_22776|HG3_Ill_GATKHC_23634|HG2_PB_assemblyticsPBcR_24666|HG3_Ill_scalpel_4797|HG2_Ill_Krunchall_4831|HG4_Ill_scalpel_1098|HG4_PB_HySA_1198|HG3_Ill_FB_3703|HG4_CG_vcfBeta_2876|HG2_Ill_SpiralSDKrefine_8241|HG3_Ill_250bpfermikitraw_4743|HG3_PB_HySA_22099|HG4_Ill_FB_9286|HG2_Ill_Krunchall_490|HG4_Ill_Cortex_3625'

df_original['New_Column'] = ""

jimb_columns = df_original.columns
df.columns = jimb_columns
print(df.head(3))
print(df.shape)
print(df_original.shape)

# print(df.columns)

df.drop('New_Column', axis=1, inplace=True)
print(df.columns)

results = df[df['variant_id'].astype(str).str.contains(matches)]


results['igv_image'] = 'images/igv_test/' + results['variant_id'] + '.jpeg'
results['gEval_image'] = 'images/gEval_test/' + results['variant_id'] + '.jpeg'
results['svviz_DotPlot_image'] = 'images/dotplots_test/' + results['variant_id'] + '.jpeg'
results['svviz_PB_image'] = 'images/PB_test/' + results['variant_id'] + '.jpeg'
results['svviz_Ill250_image'] = 'images/250bp_test/' + results['variant_id'] + '.jpeg'
results['svviz_Ill300x_image'] = 'images/300X_test/' + results['variant_id'] + '.jpeg'
results['svviz_10X_image'] = 'images/10X_test/' + results['variant_id'] + '.jpeg'
results['svviz_MP_image'] = 'images/MP_test/' + results['variant_id'] + '.jpeg'

results = results.reset_index(drop=True)
results['id'] = results.index + 1296
print(results.head(3))
print(results.tail(3))

final_df = pd.concat([df_original,results],ignore_index=True)
final_df.drop('New_Column', axis=1, inplace=True)
print(final_df.tail(3))
final_df.to_csv('test_select.csv', index=False)
# results.to_csv('JIMB_variants_select.csv', index=False)