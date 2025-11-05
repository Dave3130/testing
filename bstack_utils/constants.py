# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import os
import re
from enum import Enum
bstack1111lll11l_opy_ = {
  bstack1lll11l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ះ"): bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡳࠩៈ"),
  bstack1lll11l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ៉"): bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡫ࡦࡻࠪ៊"),
  bstack1lll11l_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫ់"): bstack1lll11l_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭៌"),
  bstack1lll11l_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪ៍"): bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫࡟ࡸ࠵ࡦࠫ៎"),
  bstack1lll11l_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪ៏"): bstack1lll11l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࠧ័"),
  bstack1lll11l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ៑"): bstack1lll11l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ្ࠧ"),
  bstack1lll11l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ៓"): bstack1lll11l_opy_ (u"ࠪࡲࡦࡳࡥࠨ។"),
  bstack1lll11l_opy_ (u"ࠫࡩ࡫ࡢࡶࡩࠪ៕"): bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡩ࡫ࡢࡶࡩࠪ៖"),
  bstack1lll11l_opy_ (u"࠭ࡣࡰࡰࡶࡳࡱ࡫ࡌࡰࡩࡶࠫៗ"): bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰࡰࡶࡳࡱ࡫ࠧ៘"),
  bstack1lll11l_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸ࠭៙"): bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸ࠭៚"),
  bstack1lll11l_opy_ (u"ࠪࡥࡵࡶࡩࡶ࡯ࡏࡳ࡬ࡹࠧ៛"): bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡵࡶࡩࡶ࡯ࡏࡳ࡬ࡹࠧៜ"),
  bstack1lll11l_opy_ (u"ࠬࡼࡩࡥࡧࡲࠫ៝"): bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡼࡩࡥࡧࡲࠫ៞"),
  bstack1lll11l_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡎࡲ࡫ࡸ࠭៟"): bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡎࡲ࡫ࡸ࠭០"),
  bstack1lll11l_opy_ (u"ࠩࡷࡩࡱ࡫࡭ࡦࡶࡵࡽࡑࡵࡧࡴࠩ១"): bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡱ࡫࡭ࡦࡶࡵࡽࡑࡵࡧࡴࠩ២"),
  bstack1lll11l_opy_ (u"ࠫ࡬࡫࡯ࡍࡱࡦࡥࡹ࡯࡯࡯ࠩ៣"): bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡬࡫࡯ࡍࡱࡦࡥࡹ࡯࡯࡯ࠩ៤"),
  bstack1lll11l_opy_ (u"࠭ࡴࡪ࡯ࡨࡾࡴࡴࡥࠨ៥"): bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡪ࡯ࡨࡾࡴࡴࡥࠨ៦"),
  bstack1lll11l_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ៧"): bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡵࡨࡰࡪࡴࡩࡶ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫ៨"),
  bstack1lll11l_opy_ (u"ࠪࡱࡦࡹ࡫ࡄࡱࡰࡱࡦࡴࡤࡴࠩ៩"): bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡱࡦࡹ࡫ࡄࡱࡰࡱࡦࡴࡤࡴࠩ៪"),
  bstack1lll11l_opy_ (u"ࠬ࡯ࡤ࡭ࡧࡗ࡭ࡲ࡫࡯ࡶࡶࠪ៫"): bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡯ࡤ࡭ࡧࡗ࡭ࡲ࡫࡯ࡶࡶࠪ៬"),
  bstack1lll11l_opy_ (u"ࠧ࡮ࡣࡶ࡯ࡇࡧࡳࡪࡥࡄࡹࡹ࡮ࠧ៭"): bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡮ࡣࡶ࡯ࡇࡧࡳࡪࡥࡄࡹࡹ࡮ࠧ៮"),
  bstack1lll11l_opy_ (u"ࠩࡶࡩࡳࡪࡋࡦࡻࡶࠫ៯"): bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡶࡩࡳࡪࡋࡦࡻࡶࠫ៰"),
  bstack1lll11l_opy_ (u"ࠫࡦࡻࡴࡰ࡙ࡤ࡭ࡹ࠭៱"): bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡻࡴࡰ࡙ࡤ࡭ࡹ࠭៲"),
  bstack1lll11l_opy_ (u"࠭ࡨࡰࡵࡷࡷࠬ៳"): bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡨࡰࡵࡷࡷࠬ៴"),
  bstack1lll11l_opy_ (u"ࠨࡤࡩࡧࡦࡩࡨࡦࠩ៵"): bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡩࡧࡦࡩࡨࡦࠩ៶"),
  bstack1lll11l_opy_ (u"ࠪࡻࡸࡒ࡯ࡤࡣ࡯ࡗࡺࡶࡰࡰࡴࡷࠫ៷"): bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡻࡸࡒ࡯ࡤࡣ࡯ࡗࡺࡶࡰࡰࡴࡷࠫ៸"),
  bstack1lll11l_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡉ࡯ࡳࡵࡕࡩࡸࡺࡲࡪࡥࡷ࡭ࡴࡴࡳࠨ៹"): bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡪࡩࡴࡣࡥࡰࡪࡉ࡯ࡳࡵࡕࡩࡸࡺࡲࡪࡥࡷ࡭ࡴࡴࡳࠨ៺"),
  bstack1lll11l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ៻"): bstack1lll11l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨ៼"),
  bstack1lll11l_opy_ (u"ࠩࡵࡩࡦࡲࡍࡰࡤ࡬ࡰࡪ࠭៽"): bstack1lll11l_opy_ (u"ࠪࡶࡪࡧ࡬ࡠ࡯ࡲࡦ࡮ࡲࡥࠨ៾"),
  bstack1lll11l_opy_ (u"ࠫࡦࡶࡰࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫ៿"): bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡶࡰࡪࡷࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ᠀"),
  bstack1lll11l_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡔࡥࡵࡹࡲࡶࡰ࠭᠁"): bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡶࡵࡷࡳࡲࡔࡥࡵࡹࡲࡶࡰ࠭᠂"),
  bstack1lll11l_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡒࡵࡳ࡫࡯࡬ࡦࠩ᠃"): bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡰࡨࡸࡼࡵࡲ࡬ࡒࡵࡳ࡫࡯࡬ࡦࠩ᠄"),
  bstack1lll11l_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡌࡲࡸ࡫ࡣࡶࡴࡨࡇࡪࡸࡴࡴࠩ᠅"): bstack1lll11l_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡗࡸࡲࡃࡦࡴࡷࡷࠬ᠆"),
  bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ᠇"): bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ᠈"),
  bstack1lll11l_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧ᠉"): bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡴࡱࡸࡶࡨ࡫ࠧ᠊"),
  bstack1lll11l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ᠋"): bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ᠌"),
  bstack1lll11l_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭᠍"): bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡭ࡵࡳࡵࡐࡤࡱࡪ࠭᠎"),
  bstack1lll11l_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪ࡙ࡩ࡮ࠩ᠏"): bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡥ࡯ࡣࡥࡰࡪ࡙ࡩ࡮ࠩ᠐"),
  bstack1lll11l_opy_ (u"ࠨࡵ࡬ࡱࡔࡶࡴࡪࡱࡱࡷࠬ᠑"): bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡵ࡬ࡱࡔࡶࡴࡪࡱࡱࡷࠬ᠒"),
  bstack1lll11l_opy_ (u"ࠪࡹࡵࡲ࡯ࡢࡦࡐࡩࡩ࡯ࡡࠨ᠓"): bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡵࡲ࡯ࡢࡦࡐࡩࡩ࡯ࡡࠨ᠔"),
  bstack1lll11l_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨ᠕"): bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨ᠖"),
  bstack1lll11l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩ᠗"): bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩ᠘")
}
bstack11l11ll1ll1_opy_ = [
  bstack1lll11l_opy_ (u"ࠩࡲࡷࠬ᠙"),
  bstack1lll11l_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭᠚"),
  bstack1lll11l_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭᠛"),
  bstack1lll11l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ᠜"),
  bstack1lll11l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪ᠝"),
  bstack1lll11l_opy_ (u"ࠧࡳࡧࡤࡰࡒࡵࡢࡪ࡮ࡨࠫ᠞"),
  bstack1lll11l_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ᠟"),
]
bstack1ll1lllll1_opy_ = {
  bstack1lll11l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᠠ"): [bstack1lll11l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡘࡗࡊࡘࡎࡂࡏࡈࠫᠡ"), bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢ࡙ࡘࡋࡒࡠࡐࡄࡑࡊ࠭ᠢ")],
  bstack1lll11l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨᠣ"): bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩᠤ"),
  bstack1lll11l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪᠥ"): bstack1lll11l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡎࡂࡏࡈࠫᠦ"),
  bstack1lll11l_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧᠧ"): bstack1lll11l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡖࡔࡐࡅࡄࡖࡢࡒࡆࡓࡅࠨᠨ"),
  bstack1lll11l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᠩ"): bstack1lll11l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧᠪ"),
  bstack1lll11l_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ᠫ"): bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡂࡔࡄࡐࡑࡋࡌࡔࡡࡓࡉࡗࡥࡐࡍࡃࡗࡊࡔࡘࡍࠨᠬ"),
  bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬᠭ"): bstack1lll11l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒࠧᠮ"),
  bstack1lll11l_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡖࡨࡷࡹࡹࠧᠯ"): bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࡡࡗࡉࡘ࡚ࡓࠨᠰ"),
  bstack1lll11l_opy_ (u"ࠬࡧࡰࡱࠩᠱ"): [bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡐࡑࡡࡌࡈࠬᠲ"), bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡑࡒࠪᠳ")],
  bstack1lll11l_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪᠴ"): bstack1lll11l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡕࡇࡏࡤࡒࡏࡈࡎࡈ࡚ࡊࡒࠧᠵ"),
  bstack1lll11l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᠶ"): bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧᠷ"),
  bstack1lll11l_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩᠸ"): [bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡓࡇ࡙ࡅࡓࡘࡄࡆࡎࡒࡉࡕ࡛ࠪᠹ"), bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡗࡋࡐࡐࡔࡗࡍࡓࡍࠧᠺ")],
  bstack1lll11l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬᠻ"): bstack1lll11l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡘࡖࡇࡕࡓࡄࡃࡏࡉࠬᠼ"),
  bstack1lll11l_opy_ (u"ࠪࡷࡲࡧࡲࡵࡕࡨࡰࡪࡩࡴࡪࡱࡱࡊࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࡨࡷࡊࡔࡖࠨᠽ"): bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡓࡗࡉࡈࡆࡕࡗࡖࡆ࡚ࡉࡐࡐࡢࡗࡒࡇࡒࡕࡡࡖࡉࡑࡋࡃࡕࡋࡒࡒࡤࡌࡅࡂࡖࡘࡖࡊࡥࡂࡓࡃࡑࡇࡍࡋࡓࠨᠾ")
}
bstack11ll1l1ll1_opy_ = {
  bstack1lll11l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧᠿ"): [bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡻࡳࡦࡴࡢࡲࡦࡳࡥࠨᡀ"), bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡵࡴࡧࡵࡒࡦࡳࡥࠨᡁ")],
  bstack1lll11l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫᡂ"): [bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡠ࡭ࡨࡽࠬᡃ"), bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬᡄ")],
  bstack1lll11l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧᡅ"): bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧᡆ"),
  bstack1lll11l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᡇ"): bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᡈ"),
  bstack1lll11l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᡉ"): bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᡊ"),
  bstack1lll11l_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᡋ"): [bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡴࡵࡶࠧᡌ"), bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫᡍ")],
  bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪᡎ"): bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬᡏ"),
  bstack1lll11l_opy_ (u"ࠨࡴࡨࡶࡺࡴࡔࡦࡵࡷࡷࠬᡐ"): bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡴࡨࡶࡺࡴࡔࡦࡵࡷࡷࠬᡑ"),
  bstack1lll11l_opy_ (u"ࠪࡥࡵࡶࠧᡒ"): bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡵࡶࠧᡓ"),
  bstack1lll11l_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧᡔ"): bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡨࡎࡨࡺࡪࡲࠧᡕ"),
  bstack1lll11l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᡖ"): bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᡗ"),
  bstack1lll11l_opy_ (u"ࠤࡶࡱࡦࡸࡴࡔࡧ࡯ࡩࡨࡺࡩࡰࡰࡉࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࡧࡶࡇࡑࡏࠢᡘ"): bstack1lll11l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠴ࡳ࡮ࡣࡵࡸࡘ࡫࡬ࡦࡥࡷ࡭ࡴࡴࡆࡦࡣࡷࡹࡷ࡫ࡂࡳࡣࡱࡧ࡭࡫ࡳࠣᡙ"),
}
bstack11lll11l1l_opy_ = {
  bstack1lll11l_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧᡚ"): bstack1lll11l_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᡛ"),
  bstack1lll11l_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᡜ"): [bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᡝ"), bstack1lll11l_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫᡞ")],
  bstack1lll11l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧᡟ"): bstack1lll11l_opy_ (u"ࠪࡲࡦࡳࡥࠨᡠ"),
  bstack1lll11l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨᡡ"): bstack1lll11l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬᡢ"),
  bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫᡣ"): [bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨᡤ"), bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡱࡥࡲ࡫ࠧᡥ")],
  bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᡦ"): bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᡧ"),
  bstack1lll11l_opy_ (u"ࠫࡷ࡫ࡡ࡭ࡏࡲࡦ࡮ࡲࡥࠨᡨ"): bstack1lll11l_opy_ (u"ࠬࡸࡥࡢ࡮ࡢࡱࡴࡨࡩ࡭ࡧࠪᡩ"),
  bstack1lll11l_opy_ (u"࠭ࡡࡱࡲ࡬ࡹࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᡪ"): [bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡱࡲ࡬ࡹࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᡫ"), bstack1lll11l_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᡬ")],
  bstack1lll11l_opy_ (u"ࠩࡤࡧࡨ࡫ࡰࡵࡋࡱࡷࡪࡩࡵࡳࡧࡆࡩࡷࡺࡳࠨᡭ"): [bstack1lll11l_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡖࡷࡱࡉࡥࡳࡶࡶࠫᡮ"), bstack1lll11l_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡗࡸࡲࡃࡦࡴࡷࠫᡯ")]
}
bstack1l1llllll_opy_ = [
  bstack1lll11l_opy_ (u"ࠬࡧࡣࡤࡧࡳࡸࡎࡴࡳࡦࡥࡸࡶࡪࡉࡥࡳࡶࡶࠫᡰ"),
  bstack1lll11l_opy_ (u"࠭ࡰࡢࡩࡨࡐࡴࡧࡤࡔࡶࡵࡥࡹ࡫ࡧࡺࠩᡱ"),
  bstack1lll11l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭ᡲ"),
  bstack1lll11l_opy_ (u"ࠨࡵࡨࡸ࡜࡯࡮ࡥࡱࡺࡖࡪࡩࡴࠨᡳ"),
  bstack1lll11l_opy_ (u"ࠩࡷ࡭ࡲ࡫࡯ࡶࡶࡶࠫᡴ"),
  bstack1lll11l_opy_ (u"ࠪࡷࡹࡸࡩࡤࡶࡉ࡭ࡱ࡫ࡉ࡯ࡶࡨࡶࡦࡩࡴࡢࡤ࡬ࡰ࡮ࡺࡹࠨᡵ"),
  bstack1lll11l_opy_ (u"ࠫࡺࡴࡨࡢࡰࡧࡰࡪࡪࡐࡳࡱࡰࡴࡹࡈࡥࡩࡣࡹ࡭ࡴࡸࠧᡶ"),
  bstack1lll11l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᡷ"),
  bstack1lll11l_opy_ (u"࠭࡭ࡰࡼ࠽ࡪ࡮ࡸࡥࡧࡱࡻࡓࡵࡺࡩࡰࡰࡶࠫᡸ"),
  bstack1lll11l_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ᡹"),
  bstack1lll11l_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ᡺"),
  bstack1lll11l_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪ࠰ࡲࡴࡹ࡯࡯࡯ࡵࠪ᡻"),
]
bstack1l1ll11ll1_opy_ = [
  bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ᡼"),
  bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ᡽"),
  bstack1lll11l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ᡾"),
  bstack1lll11l_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭᡿"),
  bstack1lll11l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪᢀ"),
  bstack1lll11l_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪᢁ"),
  bstack1lll11l_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬᢂ"),
  bstack1lll11l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧᢃ"),
  bstack1lll11l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧᢄ"),
  bstack1lll11l_opy_ (u"ࠬࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠪᢅ"),
  bstack1lll11l_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪᢆ"),
  bstack1lll11l_opy_ (u"ࠧࡵࡧࡶࡸࡗ࡫ࡰࡰࡴࡷ࡭ࡳ࡭ࠧᢇ"),
  bstack1lll11l_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠪᢈ"),
  bstack1lll11l_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡖࡤ࡫ࠬᢉ"),
  bstack1lll11l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᢊ"),
  bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᢋ"),
  bstack1lll11l_opy_ (u"ࠬࡸࡥࡳࡷࡱࡘࡪࡹࡴࡴࠩᢌ"),
  bstack1lll11l_opy_ (u"࠭ࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢ࠵ࠬᢍ"),
  bstack1lll11l_opy_ (u"ࠧࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣ࠷࠭ᢎ"),
  bstack1lll11l_opy_ (u"ࠨࡅࡘࡗ࡙ࡕࡍࡠࡖࡄࡋࡤ࠹ࠧᢏ"),
  bstack1lll11l_opy_ (u"ࠩࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࠴ࠨᢐ"),
  bstack1lll11l_opy_ (u"ࠪࡇ࡚࡙ࡔࡐࡏࡢࡘࡆࡍ࡟࠶ࠩᢑ"),
  bstack1lll11l_opy_ (u"ࠫࡈ࡛ࡓࡕࡑࡐࡣ࡙ࡇࡇࡠ࠸ࠪᢒ"),
  bstack1lll11l_opy_ (u"ࠬࡉࡕࡔࡖࡒࡑࡤ࡚ࡁࡈࡡ࠺ࠫᢓ"),
  bstack1lll11l_opy_ (u"࠭ࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢ࠼ࠬᢔ"),
  bstack1lll11l_opy_ (u"ࠧࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣ࠾࠭ᢕ"),
  bstack1lll11l_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧᢖ"),
  bstack1lll11l_opy_ (u"ࠩࡳࡩࡷࡩࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᢗ"),
  bstack1lll11l_opy_ (u"ࠪࡴࡪࡸࡣࡺࡅࡤࡴࡹࡻࡲࡦࡏࡲࡨࡪ࠭ᢘ"),
  bstack1lll11l_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡻࡴࡰࡅࡤࡴࡹࡻࡲࡦࡎࡲ࡫ࡸ࠭ᢙ"),
  bstack1lll11l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩᢚ"),
  bstack1lll11l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᢛ"),
  bstack1lll11l_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫᢜ"),
  bstack1lll11l_opy_ (u"ࠨࡪࡸࡦࡗ࡫ࡧࡪࡱࡱࠫᢝ")
]
bstack11l1l11l111_opy_ = [
  bstack1lll11l_opy_ (u"ࠩࡸࡴࡱࡵࡡࡥࡏࡨࡨ࡮ࡧࠧᢞ"),
  bstack1lll11l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬᢟ"),
  bstack1lll11l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧᢠ"),
  bstack1lll11l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪᢡ"),
  bstack1lll11l_opy_ (u"࠭ࡴࡦࡵࡷࡔࡷ࡯࡯ࡳ࡫ࡷࡽࠬᢢ"),
  bstack1lll11l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪᢣ"),
  bstack1lll11l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡔࡢࡩࠪᢤ"),
  bstack1lll11l_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧᢥ"),
  bstack1lll11l_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬᢦ"),
  bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩᢧ"),
  bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᢨ"),
  bstack1lll11l_opy_ (u"࠭࡬ࡰࡥࡤࡰᢩࠬ"),
  bstack1lll11l_opy_ (u"ࠧࡰࡵࠪᢪ"),
  bstack1lll11l_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫ᢫"),
  bstack1lll11l_opy_ (u"ࠩ࡫ࡳࡸࡺࡳࠨ᢬"),
  bstack1lll11l_opy_ (u"ࠪࡥࡺࡺ࡯ࡘࡣ࡬ࡸࠬ᢭"),
  bstack1lll11l_opy_ (u"ࠫࡷ࡫ࡧࡪࡱࡱࠫ᢮"),
  bstack1lll11l_opy_ (u"ࠬࡺࡩ࡮ࡧࡽࡳࡳ࡫ࠧ᢯"),
  bstack1lll11l_opy_ (u"࠭࡭ࡢࡥ࡫࡭ࡳ࡫ࠧᢰ"),
  bstack1lll11l_opy_ (u"ࠧࡳࡧࡶࡳࡱࡻࡴࡪࡱࡱࠫᢱ"),
  bstack1lll11l_opy_ (u"ࠨ࡫ࡧࡰࡪ࡚ࡩ࡮ࡧࡲࡹࡹ࠭ᢲ"),
  bstack1lll11l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡑࡵ࡭ࡪࡴࡴࡢࡶ࡬ࡳࡳ࠭ᢳ"),
  bstack1lll11l_opy_ (u"ࠪࡺ࡮ࡪࡥࡰࠩᢴ"),
  bstack1lll11l_opy_ (u"ࠫࡳࡵࡐࡢࡩࡨࡐࡴࡧࡤࡕ࡫ࡰࡩࡴࡻࡴࠨᢵ"),
  bstack1lll11l_opy_ (u"ࠬࡨࡦࡤࡣࡦ࡬ࡪ࠭ᢶ"),
  bstack1lll11l_opy_ (u"࠭ࡤࡦࡤࡸ࡫ࠬᢷ"),
  bstack1lll11l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡓࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫᢸ"),
  bstack1lll11l_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡔࡧࡱࡨࡐ࡫ࡹࡴࠩᢹ"),
  bstack1lll11l_opy_ (u"ࠩࡵࡩࡦࡲࡍࡰࡤ࡬ࡰࡪ࠭ᢺ"),
  bstack1lll11l_opy_ (u"ࠪࡲࡴࡖࡩࡱࡧ࡯࡭ࡳ࡫ࠧᢻ"),
  bstack1lll11l_opy_ (u"ࠫࡨ࡮ࡥࡤ࡭ࡘࡖࡑ࠭ᢼ"),
  bstack1lll11l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᢽ"),
  bstack1lll11l_opy_ (u"࠭ࡡࡤࡥࡨࡴࡹࡉ࡯ࡰ࡭࡬ࡩࡸ࠭ᢾ"),
  bstack1lll11l_opy_ (u"ࠧࡤࡣࡳࡸࡺࡸࡥࡄࡴࡤࡷ࡭࠭ᢿ"),
  bstack1lll11l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬᣀ"),
  bstack1lll11l_opy_ (u"ࠩࡤࡴࡵ࡯ࡵ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩᣁ"),
  bstack1lll11l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࡖࡦࡴࡶ࡭ࡴࡴࠧᣂ"),
  bstack1lll11l_opy_ (u"ࠫࡳࡵࡂ࡭ࡣࡱ࡯ࡕࡵ࡬࡭࡫ࡱ࡫ࠬᣃ"),
  bstack1lll11l_opy_ (u"ࠬࡳࡡࡴ࡭ࡖࡩࡳࡪࡋࡦࡻࡶࠫᣄ"),
  bstack1lll11l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡒ࡯ࡨࡵࠪᣅ"),
  bstack1lll11l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡉࡥࠩᣆ"),
  bstack1lll11l_opy_ (u"ࠨࡦࡨࡨ࡮ࡩࡡࡵࡧࡧࡈࡪࡼࡩࡤࡧࠪᣇ"),
  bstack1lll11l_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡒࡤࡶࡦࡳࡳࠨᣈ"),
  bstack1lll11l_opy_ (u"ࠪࡴ࡭ࡵ࡮ࡦࡐࡸࡱࡧ࡫ࡲࠨᣉ"),
  bstack1lll11l_opy_ (u"ࠫࡳ࡫ࡴࡸࡱࡵ࡯ࡑࡵࡧࡴࠩᣊ"),
  bstack1lll11l_opy_ (u"ࠬࡴࡥࡵࡹࡲࡶࡰࡒ࡯ࡨࡵࡒࡴࡹ࡯࡯࡯ࡵࠪᣋ"),
  bstack1lll11l_opy_ (u"࠭ࡣࡰࡰࡶࡳࡱ࡫ࡌࡰࡩࡶࠫᣌ"),
  bstack1lll11l_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧᣍ"),
  bstack1lll11l_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡍࡱࡪࡷࠬᣎ"),
  bstack1lll11l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡄ࡬ࡳࡲ࡫ࡴࡳ࡫ࡦࠫᣏ"),
  bstack1lll11l_opy_ (u"ࠪࡺ࡮ࡪࡥࡰࡘ࠵ࠫᣐ"),
  bstack1lll11l_opy_ (u"ࠫࡲ࡯ࡤࡔࡧࡶࡷ࡮ࡵ࡮ࡊࡰࡶࡸࡦࡲ࡬ࡂࡲࡳࡷࠬᣑ"),
  bstack1lll11l_opy_ (u"ࠬ࡫ࡳࡱࡴࡨࡷࡸࡵࡓࡦࡴࡹࡩࡷ࠭ᣒ"),
  bstack1lll11l_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡍࡱࡪࡷࠬᣓ"),
  bstack1lll11l_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡅࡧࡴࠬᣔ"),
  bstack1lll11l_opy_ (u"ࠨࡶࡨࡰࡪࡳࡥࡵࡴࡼࡐࡴ࡭ࡳࠨᣕ"),
  bstack1lll11l_opy_ (u"ࠩࡶࡽࡳࡩࡔࡪ࡯ࡨ࡛࡮ࡺࡨࡏࡖࡓࠫᣖ"),
  bstack1lll11l_opy_ (u"ࠪ࡫ࡪࡵࡌࡰࡥࡤࡸ࡮ࡵ࡮ࠨᣗ"),
  bstack1lll11l_opy_ (u"ࠫ࡬ࡶࡳࡍࡱࡦࡥࡹ࡯࡯࡯ࠩᣘ"),
  bstack1lll11l_opy_ (u"ࠬࡴࡥࡵࡹࡲࡶࡰࡖࡲࡰࡨ࡬ࡰࡪ࠭ᣙ"),
  bstack1lll11l_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡔࡥࡵࡹࡲࡶࡰ࠭ᣚ"),
  bstack1lll11l_opy_ (u"ࠧࡧࡱࡵࡧࡪࡉࡨࡢࡰࡪࡩࡏࡧࡲࠨᣛ"),
  bstack1lll11l_opy_ (u"ࠨࡺࡰࡷࡏࡧࡲࠨᣜ"),
  bstack1lll11l_opy_ (u"ࠩࡻࡱࡽࡐࡡࡳࠩᣝ"),
  bstack1lll11l_opy_ (u"ࠪࡱࡦࡹ࡫ࡄࡱࡰࡱࡦࡴࡤࡴࠩᣞ"),
  bstack1lll11l_opy_ (u"ࠫࡲࡧࡳ࡬ࡄࡤࡷ࡮ࡩࡁࡶࡶ࡫ࠫᣟ"),
  bstack1lll11l_opy_ (u"ࠬࡽࡳࡍࡱࡦࡥࡱ࡙ࡵࡱࡲࡲࡶࡹ࠭ᣠ"),
  bstack1lll11l_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡃࡰࡴࡶࡖࡪࡹࡴࡳ࡫ࡦࡸ࡮ࡵ࡮ࡴࠩᣡ"),
  bstack1lll11l_opy_ (u"ࠧࡢࡲࡳ࡚ࡪࡸࡳࡪࡱࡱࠫᣢ"),
  bstack1lll11l_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡊࡰࡶࡩࡨࡻࡲࡦࡅࡨࡶࡹࡹࠧᣣ"),
  bstack1lll11l_opy_ (u"ࠩࡵࡩࡸ࡯ࡧ࡯ࡃࡳࡴࠬᣤ"),
  bstack1lll11l_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡳ࡯࡭ࡢࡶ࡬ࡳࡳࡹࠧᣥ"),
  bstack1lll11l_opy_ (u"ࠫࡨࡧ࡮ࡢࡴࡼࠫᣦ"),
  bstack1lll11l_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭ᣧ"),
  bstack1lll11l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭ᣨ"),
  bstack1lll11l_opy_ (u"ࠧࡪࡧࠪᣩ"),
  bstack1lll11l_opy_ (u"ࠨࡧࡧ࡫ࡪ࠭ᣪ"),
  bstack1lll11l_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࠩᣫ"),
  bstack1lll11l_opy_ (u"ࠪࡵࡺ࡫ࡵࡦࠩᣬ"),
  bstack1lll11l_opy_ (u"ࠫ࡮ࡴࡴࡦࡴࡱࡥࡱ࠭ᣭ"),
  bstack1lll11l_opy_ (u"ࠬࡧࡰࡱࡕࡷࡳࡷ࡫ࡃࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳ࠭ᣮ"),
  bstack1lll11l_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡉࡡ࡮ࡧࡵࡥࡎࡳࡡࡨࡧࡌࡲ࡯࡫ࡣࡵ࡫ࡲࡲࠬᣯ"),
  bstack1lll11l_opy_ (u"ࠧ࡯ࡧࡷࡻࡴࡸ࡫ࡍࡱࡪࡷࡊࡾࡣ࡭ࡷࡧࡩࡍࡵࡳࡵࡵࠪᣰ"),
  bstack1lll11l_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸࡏ࡮ࡤ࡮ࡸࡨࡪࡎ࡯ࡴࡶࡶࠫᣱ"),
  bstack1lll11l_opy_ (u"ࠩࡸࡴࡩࡧࡴࡦࡃࡳࡴࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸ࠭ᣲ"),
  bstack1lll11l_opy_ (u"ࠪࡶࡪࡹࡥࡳࡸࡨࡈࡪࡼࡩࡤࡧࠪᣳ"),
  bstack1lll11l_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫᣴ"),
  bstack1lll11l_opy_ (u"ࠬࡹࡥ࡯ࡦࡎࡩࡾࡹࠧᣵ"),
  bstack1lll11l_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡖࡡࡴࡵࡦࡳࡩ࡫ࠧ᣶"),
  bstack1lll11l_opy_ (u"ࠧࡶࡲࡧࡥࡹ࡫ࡉࡰࡵࡇࡩࡻ࡯ࡣࡦࡕࡨࡸࡹ࡯࡮ࡨࡵࠪ᣷"),
  bstack1lll11l_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡂࡷࡧ࡭ࡴࡏ࡮࡫ࡧࡦࡸ࡮ࡵ࡮ࠨ᣸"),
  bstack1lll11l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡃࡳࡴࡱ࡫ࡐࡢࡻࠪ᣹"),
  bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫ᣺"),
  bstack1lll11l_opy_ (u"ࠫࡼࡪࡩࡰࡕࡨࡶࡻ࡯ࡣࡦࠩ᣻"),
  bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ᣼"),
  bstack1lll11l_opy_ (u"࠭ࡰࡳࡧࡹࡩࡳࡺࡃࡳࡱࡶࡷࡘ࡯ࡴࡦࡖࡵࡥࡨࡱࡩ࡯ࡩࠪ᣽"),
  bstack1lll11l_opy_ (u"ࠧࡩ࡫ࡪ࡬ࡈࡵ࡮ࡵࡴࡤࡷࡹ࠭᣾"),
  bstack1lll11l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡑࡴࡨࡪࡪࡸࡥ࡯ࡥࡨࡷࠬ᣿"),
  bstack1lll11l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡕ࡬ࡱࠬᤀ"),
  bstack1lll11l_opy_ (u"ࠪࡷ࡮ࡳࡏࡱࡶ࡬ࡳࡳࡹࠧᤁ"),
  bstack1lll11l_opy_ (u"ࠫࡷ࡫࡭ࡰࡸࡨࡍࡔ࡙ࡁࡱࡲࡖࡩࡹࡺࡩ࡯ࡩࡶࡐࡴࡩࡡ࡭࡫ࡽࡥࡹ࡯࡯࡯ࠩᤂ"),
  bstack1lll11l_opy_ (u"ࠬ࡮࡯ࡴࡶࡑࡥࡲ࡫ࠧᤃ"),
  bstack1lll11l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᤄ"),
  bstack1lll11l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩᤅ"),
  bstack1lll11l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠧᤆ"),
  bstack1lll11l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫᤇ"),
  bstack1lll11l_opy_ (u"ࠪࡴࡦ࡭ࡥࡍࡱࡤࡨࡘࡺࡲࡢࡶࡨ࡫ࡾ࠭ᤈ"),
  bstack1lll11l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪᤉ"),
  bstack1lll11l_opy_ (u"ࠬࡺࡩ࡮ࡧࡲࡹࡹࡹࠧᤊ"),
  bstack1lll11l_opy_ (u"࠭ࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࡒࡵࡳࡲࡶࡴࡃࡧ࡫ࡥࡻ࡯࡯ࡳࠩᤋ")
]
bstack111l1l1lll_opy_ = {
  bstack1lll11l_opy_ (u"ࠧࡷࠩᤌ"): bstack1lll11l_opy_ (u"ࠨࡸࠪᤍ"),
  bstack1lll11l_opy_ (u"ࠩࡩࠫᤎ"): bstack1lll11l_opy_ (u"ࠪࡪࠬᤏ"),
  bstack1lll11l_opy_ (u"ࠫ࡫ࡵࡲࡤࡧࠪᤐ"): bstack1lll11l_opy_ (u"ࠬ࡬࡯ࡳࡥࡨࠫᤑ"),
  bstack1lll11l_opy_ (u"࠭࡯࡯࡮ࡼࡥࡺࡺ࡯࡮ࡣࡷࡩࠬᤒ"): bstack1lll11l_opy_ (u"ࠧࡰࡰ࡯ࡽࡆࡻࡴࡰ࡯ࡤࡸࡪ࠭ᤓ"),
  bstack1lll11l_opy_ (u"ࠨࡨࡲࡶࡨ࡫࡬ࡰࡥࡤࡰࠬᤔ"): bstack1lll11l_opy_ (u"ࠩࡩࡳࡷࡩࡥ࡭ࡱࡦࡥࡱ࠭ᤕ"),
  bstack1lll11l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡪࡲࡷࡹ࠭ᤖ"): bstack1lll11l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡋࡳࡸࡺࠧᤗ"),
  bstack1lll11l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡴࡴࡸࡴࠨᤘ"): bstack1lll11l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡵࡲࡵࠩᤙ"),
  bstack1lll11l_opy_ (u"ࠧࡱࡴࡲࡼࡾࡻࡳࡦࡴࠪᤚ"): bstack1lll11l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡕࡴࡧࡵࠫᤛ"),
  bstack1lll11l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡱࡣࡶࡷࠬᤜ"): bstack1lll11l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡤࡷࡸ࠭ᤝ"),
  bstack1lll11l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡳࡶࡴࡾࡹࡩࡱࡶࡸࠬᤞ"): bstack1lll11l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡔࡷࡵࡸࡺࡊࡲࡷࡹ࠭᤟"),
  bstack1lll11l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡵࡸ࡯ࡹࡻࡳࡳࡷࡺࠧᤠ"): bstack1lll11l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡖࡲࡰࡺࡼࡔࡴࡸࡴࠨᤡ"),
  bstack1lll11l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡰࡳࡱࡻࡽࡺࡹࡥࡳࠩᤢ"): bstack1lll11l_opy_ (u"ࠩ࠰ࡰࡴࡩࡡ࡭ࡒࡵࡳࡽࡿࡕࡴࡧࡵࠫᤣ"),
  bstack1lll11l_opy_ (u"ࠪ࠱ࡱࡵࡣࡢ࡮ࡳࡶࡴࡾࡹࡶࡵࡨࡶࠬᤤ"): bstack1lll11l_opy_ (u"ࠫ࠲ࡲ࡯ࡤࡣ࡯ࡔࡷࡵࡸࡺࡗࡶࡩࡷ࠭ᤥ"),
  bstack1lll11l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡴࡷࡵࡸࡺࡲࡤࡷࡸ࠭ᤦ"): bstack1lll11l_opy_ (u"࠭࠭࡭ࡱࡦࡥࡱࡖࡲࡰࡺࡼࡔࡦࡹࡳࠨᤧ"),
  bstack1lll11l_opy_ (u"ࠧ࠮࡮ࡲࡧࡦࡲࡰࡳࡱࡻࡽࡵࡧࡳࡴࠩᤨ"): bstack1lll11l_opy_ (u"ࠨ࠯࡯ࡳࡨࡧ࡬ࡑࡴࡲࡼࡾࡖࡡࡴࡵࠪᤩ"),
  bstack1lll11l_opy_ (u"ࠩࡥ࡭ࡳࡧࡲࡺࡲࡤࡸ࡭࠭ᤪ"): bstack1lll11l_opy_ (u"ࠪࡦ࡮ࡴࡡࡳࡻࡳࡥࡹ࡮ࠧᤫ"),
  bstack1lll11l_opy_ (u"ࠫࡵࡧࡣࡧ࡫࡯ࡩࠬ᤬"): bstack1lll11l_opy_ (u"ࠬ࠳ࡰࡢࡥ࠰ࡪ࡮ࡲࡥࠨ᤭"),
  bstack1lll11l_opy_ (u"࠭ࡰࡢࡥ࠰ࡪ࡮ࡲࡥࠨ᤮"): bstack1lll11l_opy_ (u"ࠧ࠮ࡲࡤࡧ࠲࡬ࡩ࡭ࡧࠪ᤯"),
  bstack1lll11l_opy_ (u"ࠨ࠯ࡳࡥࡨ࠳ࡦࡪ࡮ࡨࠫᤰ"): bstack1lll11l_opy_ (u"ࠩ࠰ࡴࡦࡩ࠭ࡧ࡫࡯ࡩࠬᤱ"),
  bstack1lll11l_opy_ (u"ࠪࡰࡴ࡭ࡦࡪ࡮ࡨࠫᤲ"): bstack1lll11l_opy_ (u"ࠫࡱࡵࡧࡧ࡫࡯ࡩࠬᤳ"),
  bstack1lll11l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᤴ"): bstack1lll11l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᤵ"),
  bstack1lll11l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࠭ࡳࡧࡳࡩࡦࡺࡥࡳࠩᤶ"): bstack1lll11l_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡓࡧࡳࡩࡦࡺࡥࡳࠩᤷ")
}
bstack11l1l11l1l1_opy_ = bstack1lll11l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲࡫࡮ࡺࡨࡶࡤ࠱ࡧࡴࡳ࠯ࡱࡧࡵࡧࡾ࠵ࡣ࡭࡫࠲ࡶࡪࡲࡥࡢࡵࡨࡷ࠴ࡲࡡࡵࡧࡶࡸ࠴ࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠢᤸ")
bstack11l11lll111_opy_ = bstack1lll11l_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠲࡬ࡪࡧ࡬ࡵࡪࡦ࡬ࡪࡩ࡫᤹ࠣ")
bstack1lll11ll11_opy_ = bstack1lll11l_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴࡫ࡤࡴ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡹࡥ࡯ࡦࡢࡷࡩࡱ࡟ࡦࡸࡨࡲࡹࡹࠢ᤺")
bstack1ll1llllll_opy_ = bstack1lll11l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡨࡶࡤ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡷࡥ࠱࡫ࡹࡧ᤻࠭")
bstack11l1l111ll_opy_ = bstack1lll11l_opy_ (u"࠭ࡨࡵࡶࡳ࠾࠴࠵ࡨࡶࡤ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠩ᤼")
bstack1llll1ll11_opy_ = bstack1lll11l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡪࡸࡦ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡰࡨࡼࡹࡥࡨࡶࡤࡶࠫ᤽")
bstack1lll11l1l1_opy_ = {
  bstack1lll11l_opy_ (u"ࠨࡦࡨࡪࡦࡻ࡬ࡵࠩ᤾"): bstack1lll11l_opy_ (u"ࠩ࡫ࡹࡧ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩ᤿"),
  bstack1lll11l_opy_ (u"ࠪࡹࡸ࠳ࡥࡢࡵࡷࠫ᥀"): bstack1lll11l_opy_ (u"ࠫ࡭ࡻࡢ࠮ࡷࡶࡩ࠲ࡵ࡮࡭ࡻ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭᥁"),
  bstack1lll11l_opy_ (u"ࠬࡻࡳࠨ᥂"): bstack1lll11l_opy_ (u"࠭ࡨࡶࡤ࠰ࡹࡸ࠳࡯࡯࡮ࡼ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧ᥃"),
  bstack1lll11l_opy_ (u"ࠧࡦࡷࠪ᥄"): bstack1lll11l_opy_ (u"ࠨࡪࡸࡦ࠲࡫ࡵ࠮ࡱࡱࡰࡾ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩ᥅"),
  bstack1lll11l_opy_ (u"ࠩ࡬ࡲࠬ᥆"): bstack1lll11l_opy_ (u"ࠪ࡬ࡺࡨ࠭ࡢࡲࡶ࠱ࡴࡴ࡬ࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ᥇"),
  bstack1lll11l_opy_ (u"ࠫࡦࡻࠧ᥈"): bstack1lll11l_opy_ (u"ࠬ࡮ࡵࡣ࠯ࡤࡴࡸ࡫࠭ࡰࡰ࡯ࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨ᥉")
}
bstack11l1l11111l_opy_ = {
  bstack1lll11l_opy_ (u"࠭ࡣࡳ࡫ࡷ࡭ࡨࡧ࡬ࠨ᥊"): 50,
  bstack1lll11l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭᥋"): 40,
  bstack1lll11l_opy_ (u"ࠨࡹࡤࡶࡳ࡯࡮ࡨࠩ᥌"): 30,
  bstack1lll11l_opy_ (u"ࠩ࡬ࡲ࡫ࡵࠧ᥍"): 20,
  bstack1lll11l_opy_ (u"ࠪࡨࡪࡨࡵࡨࠩ᥎"): 10
}
bstack11l11ll11_opy_ = bstack11l1l11111l_opy_[bstack1lll11l_opy_ (u"ࠫ࡮ࡴࡦࡰࠩ᥏")]
bstack111l1llll1_opy_ = bstack1lll11l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠲ࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࠫᥐ")
bstack111l11l1l_opy_ = bstack1lll11l_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲ࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࠫᥑ")
bstack1lll1lllll_opy_ = bstack1lll11l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫࠭ࡱࡻࡷ࡬ࡴࡴࡡࡨࡧࡱࡸ࠴࠭ᥒ")
bstack1lllll1ll1_opy_ = bstack1lll11l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡲࡼࡸ࡭ࡵ࡮ࡢࡩࡨࡲࡹ࠵ࠧᥓ")
bstack1llll11ll_opy_ = bstack1lll11l_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶࠣࡥࡳࡪࠠࡱࡻࡷࡩࡸࡺ࠭ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠢࡳࡥࡨࡱࡡࡨࡧࡶ࠲ࠥࡦࡰࡪࡲࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡵࡿࡴࡦࡵࡷࠤࡵࡿࡴࡦࡵࡷ࠱ࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡦࠧᥔ")
bstack11l1l1111ll_opy_ = [bstack1lll11l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡘࡗࡊࡘࡎࡂࡏࡈࠫᥕ"), bstack1lll11l_opy_ (u"ࠫ࡞ࡕࡕࡓࡡࡘࡗࡊࡘࡎࡂࡏࡈࠫᥖ")]
bstack11l1l111lll_opy_ = [bstack1lll11l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆࡉࡃࡆࡕࡖࡣࡐࡋ࡙ࠨᥗ"), bstack1lll11l_opy_ (u"࡙࠭ࡐࡗࡕࡣࡆࡉࡃࡆࡕࡖࡣࡐࡋ࡙ࠨᥘ")]
bstack1l1l1ll1ll_opy_ = re.compile(bstack1lll11l_opy_ (u"ࠧ࡟࡝࡟ࡠࡼ࠳࡝ࠬ࠼࠱࠮ࠩ࠭ᥙ"))
bstack11lll1l1l_opy_ = [
  bstack1lll11l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡓࡧ࡭ࡦࠩᥚ"),
  bstack1lll11l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫᥛ"),
  bstack1lll11l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧᥜ"),
  bstack1lll11l_opy_ (u"ࠫࡳ࡫ࡷࡄࡱࡰࡱࡦࡴࡤࡕ࡫ࡰࡩࡴࡻࡴࠨᥝ"),
  bstack1lll11l_opy_ (u"ࠬࡧࡰࡱࠩᥞ"),
  bstack1lll11l_opy_ (u"࠭ࡵࡥ࡫ࡧࠫᥟ"),
  bstack1lll11l_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࠩᥠ"),
  bstack1lll11l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡥࠨᥡ"),
  bstack1lll11l_opy_ (u"ࠩࡲࡶ࡮࡫࡮ࡵࡣࡷ࡭ࡴࡴࠧᥢ"),
  bstack1lll11l_opy_ (u"ࠪࡥࡺࡺ࡯ࡘࡧࡥࡺ࡮࡫ࡷࠨᥣ"),
  bstack1lll11l_opy_ (u"ࠫࡳࡵࡒࡦࡵࡨࡸࠬᥤ"), bstack1lll11l_opy_ (u"ࠬ࡬ࡵ࡭࡮ࡕࡩࡸ࡫ࡴࠨᥥ"),
  bstack1lll11l_opy_ (u"࠭ࡣ࡭ࡧࡤࡶࡘࡿࡳࡵࡧࡰࡊ࡮ࡲࡥࡴࠩᥦ"),
  bstack1lll11l_opy_ (u"ࠧࡦࡸࡨࡲࡹ࡚ࡩ࡮࡫ࡱ࡫ࡸ࠭ᥧ"),
  bstack1lll11l_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡑࡧࡵࡪࡴࡸ࡭ࡢࡰࡦࡩࡑࡵࡧࡨ࡫ࡱ࡫ࠬᥨ"),
  bstack1lll11l_opy_ (u"ࠩࡲࡸ࡭࡫ࡲࡂࡲࡳࡷࠬᥩ"),
  bstack1lll11l_opy_ (u"ࠪࡴࡷ࡯࡮ࡵࡒࡤ࡫ࡪ࡙࡯ࡶࡴࡦࡩࡔࡴࡆࡪࡰࡧࡊࡦ࡯࡬ࡶࡴࡨࠫᥪ"),
  bstack1lll11l_opy_ (u"ࠫࡦࡶࡰࡂࡥࡷ࡭ࡻ࡯ࡴࡺࠩᥫ"), bstack1lll11l_opy_ (u"ࠬࡧࡰࡱࡒࡤࡧࡰࡧࡧࡦࠩᥬ"), bstack1lll11l_opy_ (u"࠭ࡡࡱࡲ࡚ࡥ࡮ࡺࡁࡤࡶ࡬ࡺ࡮ࡺࡹࠨᥭ"), bstack1lll11l_opy_ (u"ࠧࡢࡲࡳ࡛ࡦ࡯ࡴࡑࡣࡦ࡯ࡦ࡭ࡥࠨ᥮"), bstack1lll11l_opy_ (u"ࠨࡣࡳࡴ࡜ࡧࡩࡵࡆࡸࡶࡦࡺࡩࡰࡰࠪ᥯"),
  bstack1lll11l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡔࡨࡥࡩࡿࡔࡪ࡯ࡨࡳࡺࡺࠧᥰ"),
  bstack1lll11l_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡖࡨࡷࡹࡖࡡࡤ࡭ࡤ࡫ࡪࡹࠧᥱ"),
  bstack1lll11l_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࡈࡵࡶࡦࡴࡤ࡫ࡪ࠭ᥲ"), bstack1lll11l_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩࡉ࡯ࡷࡧࡵࡥ࡬࡫ࡅ࡯ࡦࡌࡲࡹ࡫࡮ࡵࠩᥳ"),
  bstack1lll11l_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࡄࡦࡸ࡬ࡧࡪࡘࡥࡢࡦࡼࡘ࡮ࡳࡥࡰࡷࡷࠫᥴ"),
  bstack1lll11l_opy_ (u"ࠧࡢࡦࡥࡔࡴࡸࡴࠨ᥵"),
  bstack1lll11l_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࡆࡨࡺ࡮ࡩࡥࡔࡱࡦ࡯ࡪࡺࠧ᥶"),
  bstack1lll11l_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡌࡲࡸࡺࡡ࡭࡮ࡗ࡭ࡲ࡫࡯ࡶࡶࠪ᥷"),
  bstack1lll11l_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࡍࡳࡹࡴࡢ࡮࡯ࡔࡦࡺࡨࠨ᥸"),
  bstack1lll11l_opy_ (u"ࠫࡦࡼࡤࠨ᥹"), bstack1lll11l_opy_ (u"ࠬࡧࡶࡥࡎࡤࡹࡳࡩࡨࡕ࡫ࡰࡩࡴࡻࡴࠨ᥺"), bstack1lll11l_opy_ (u"࠭ࡡࡷࡦࡕࡩࡦࡪࡹࡕ࡫ࡰࡩࡴࡻࡴࠨ᥻"), bstack1lll11l_opy_ (u"ࠧࡢࡸࡧࡅࡷ࡭ࡳࠨ᥼"),
  bstack1lll11l_opy_ (u"ࠨࡷࡶࡩࡐ࡫ࡹࡴࡶࡲࡶࡪ࠭᥽"), bstack1lll11l_opy_ (u"ࠩ࡮ࡩࡾࡹࡴࡰࡴࡨࡔࡦࡺࡨࠨ᥾"), bstack1lll11l_opy_ (u"ࠪ࡯ࡪࡿࡳࡵࡱࡵࡩࡕࡧࡳࡴࡹࡲࡶࡩ࠭᥿"),
  bstack1lll11l_opy_ (u"ࠫࡰ࡫ࡹࡂ࡮࡬ࡥࡸ࠭ᦀ"), bstack1lll11l_opy_ (u"ࠬࡱࡥࡺࡒࡤࡷࡸࡽ࡯ࡳࡦࠪᦁ"),
  bstack1lll11l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡪࡲࡪࡸࡨࡶࡊࡾࡥࡤࡷࡷࡥࡧࡲࡥࠨᦂ"), bstack1lll11l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷࡇࡲࡨࡵࠪᦃ"), bstack1lll11l_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡥࡴ࡬ࡺࡪࡸࡅࡹࡧࡦࡹࡹࡧࡢ࡭ࡧࡇ࡭ࡷ࠭ᦄ"), bstack1lll11l_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡦࡵ࡭ࡻ࡫ࡲࡄࡪࡵࡳࡲ࡫ࡍࡢࡲࡳ࡭ࡳ࡭ࡆࡪ࡮ࡨࠫᦅ"), bstack1lll11l_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡧࡶ࡮ࡼࡥࡳࡗࡶࡩࡘࡿࡳࡵࡧࡰࡉࡽ࡫ࡣࡶࡶࡤࡦࡱ࡫ࠧᦆ"),
  bstack1lll11l_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡨࡷ࡯ࡶࡦࡴࡓࡳࡷࡺࠧᦇ"), bstack1lll11l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡩࡸࡩࡷࡧࡵࡔࡴࡸࡴࡴࠩᦈ"),
  bstack1lll11l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡪࡲࡪࡸࡨࡶࡉ࡯ࡳࡢࡤ࡯ࡩࡇࡻࡩ࡭ࡦࡆ࡬ࡪࡩ࡫ࠨᦉ"),
  bstack1lll11l_opy_ (u"ࠧࡢࡷࡷࡳ࡜࡫ࡢࡷ࡫ࡨࡻ࡙࡯࡭ࡦࡱࡸࡸࠬᦊ"),
  bstack1lll11l_opy_ (u"ࠨ࡫ࡱࡸࡪࡴࡴࡂࡥࡷ࡭ࡴࡴࠧᦋ"), bstack1lll11l_opy_ (u"ࠩ࡬ࡲࡹ࡫࡮ࡵࡅࡤࡸࡪ࡭࡯ࡳࡻࠪᦌ"), bstack1lll11l_opy_ (u"ࠪ࡭ࡳࡺࡥ࡯ࡶࡉࡰࡦ࡭ࡳࠨᦍ"), bstack1lll11l_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡥࡱࡏ࡮ࡵࡧࡱࡸࡆࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᦎ"),
  bstack1lll11l_opy_ (u"ࠬࡪ࡯࡯ࡶࡖࡸࡴࡶࡁࡱࡲࡒࡲࡗ࡫ࡳࡦࡶࠪᦏ"),
  bstack1lll11l_opy_ (u"࠭ࡵ࡯࡫ࡦࡳࡩ࡫ࡋࡦࡻࡥࡳࡦࡸࡤࠨᦐ"), bstack1lll11l_opy_ (u"ࠧࡳࡧࡶࡩࡹࡑࡥࡺࡤࡲࡥࡷࡪࠧᦑ"),
  bstack1lll11l_opy_ (u"ࠨࡰࡲࡗ࡮࡭࡮ࠨᦒ"),
  bstack1lll11l_opy_ (u"ࠩ࡬࡫ࡳࡵࡲࡦࡗࡱ࡭ࡲࡶ࡯ࡳࡶࡤࡲࡹ࡜ࡩࡦࡹࡶࠫᦓ"),
  bstack1lll11l_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡳࡪࡲࡰ࡫ࡧ࡛ࡦࡺࡣࡩࡧࡵࡷࠬᦔ"),
  bstack1lll11l_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫᦕ"),
  bstack1lll11l_opy_ (u"ࠬࡸࡥࡤࡴࡨࡥࡹ࡫ࡃࡩࡴࡲࡱࡪࡊࡲࡪࡸࡨࡶࡘ࡫ࡳࡴ࡫ࡲࡲࡸ࠭ᦖ"),
  bstack1lll11l_opy_ (u"࠭࡮ࡢࡶ࡬ࡺࡪ࡝ࡥࡣࡕࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬᦗ"),
  bstack1lll11l_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࡔࡥࡵࡩࡪࡴࡳࡩࡱࡷࡔࡦࡺࡨࠨᦘ"),
  bstack1lll11l_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡕࡳࡩࡪࡪࠧᦙ"),
  bstack1lll11l_opy_ (u"ࠩࡪࡴࡸࡋ࡮ࡢࡤ࡯ࡩࡩ࠭ᦚ"),
  bstack1lll11l_opy_ (u"ࠪ࡭ࡸࡎࡥࡢࡦ࡯ࡩࡸࡹࠧᦛ"),
  bstack1lll11l_opy_ (u"ࠫࡦࡪࡢࡆࡺࡨࡧ࡙࡯࡭ࡦࡱࡸࡸࠬᦜ"),
  bstack1lll11l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡩࡘࡩࡲࡪࡲࡷࠫᦝ"),
  bstack1lll11l_opy_ (u"࠭ࡳ࡬࡫ࡳࡈࡪࡼࡩࡤࡧࡌࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡦࡺࡩࡰࡰࠪᦞ"),
  bstack1lll11l_opy_ (u"ࠧࡢࡷࡷࡳࡌࡸࡡ࡯ࡶࡓࡩࡷࡳࡩࡴࡵ࡬ࡳࡳࡹࠧᦟ"),
  bstack1lll11l_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࡐࡤࡸࡺࡸࡡ࡭ࡑࡵ࡭ࡪࡴࡴࡢࡶ࡬ࡳࡳ࠭ᦠ"),
  bstack1lll11l_opy_ (u"ࠩࡶࡽࡸࡺࡥ࡮ࡒࡲࡶࡹ࠭ᦡ"),
  bstack1lll11l_opy_ (u"ࠪࡶࡪࡳ࡯ࡵࡧࡄࡨࡧࡎ࡯ࡴࡶࠪᦢ"),
  bstack1lll11l_opy_ (u"ࠫࡸࡱࡩࡱࡗࡱࡰࡴࡩ࡫ࠨᦣ"), bstack1lll11l_opy_ (u"ࠬࡻ࡮࡭ࡱࡦ࡯࡙ࡿࡰࡦࠩᦤ"), bstack1lll11l_opy_ (u"࠭ࡵ࡯࡮ࡲࡧࡰࡑࡥࡺࠩᦥ"),
  bstack1lll11l_opy_ (u"ࠧࡢࡷࡷࡳࡑࡧࡵ࡯ࡥ࡫ࠫᦦ"),
  bstack1lll11l_opy_ (u"ࠨࡵ࡮࡭ࡵࡒ࡯ࡨࡥࡤࡸࡈࡧࡰࡵࡷࡵࡩࠬᦧ"),
  bstack1lll11l_opy_ (u"ࠩࡸࡲ࡮ࡴࡳࡵࡣ࡯ࡰࡔࡺࡨࡦࡴࡓࡥࡨࡱࡡࡨࡧࡶࠫᦨ"),
  bstack1lll11l_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨ࡛࡮ࡴࡤࡰࡹࡄࡲ࡮ࡳࡡࡵ࡫ࡲࡲࠬᦩ"),
  bstack1lll11l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡗࡳࡴࡲࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨᦪ"),
  bstack1lll11l_opy_ (u"ࠬ࡫࡮ࡧࡱࡵࡧࡪࡇࡰࡱࡋࡱࡷࡹࡧ࡬࡭ࠩᦫ"),
  bstack1lll11l_opy_ (u"࠭ࡥ࡯ࡵࡸࡶࡪ࡝ࡥࡣࡸ࡬ࡩࡼࡹࡈࡢࡸࡨࡔࡦ࡭ࡥࡴࠩ᦬"), bstack1lll11l_opy_ (u"ࠧࡸࡧࡥࡺ࡮࡫ࡷࡅࡧࡹࡸࡴࡵ࡬ࡴࡒࡲࡶࡹ࠭᦭"), bstack1lll11l_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡘࡧࡥࡺ࡮࡫ࡷࡅࡧࡷࡥ࡮ࡲࡳࡄࡱ࡯ࡰࡪࡩࡴࡪࡱࡱࠫ᦮"),
  bstack1lll11l_opy_ (u"ࠩࡵࡩࡲࡵࡴࡦࡃࡳࡴࡸࡉࡡࡤࡪࡨࡐ࡮ࡳࡩࡵࠩ᦯"),
  bstack1lll11l_opy_ (u"ࠪࡧࡦࡲࡥ࡯ࡦࡤࡶࡋࡵࡲ࡮ࡣࡷࠫᦰ"),
  bstack1lll11l_opy_ (u"ࠫࡧࡻ࡮ࡥ࡮ࡨࡍࡩ࠭ᦱ"),
  bstack1lll11l_opy_ (u"ࠬࡲࡡࡶࡰࡦ࡬࡙࡯࡭ࡦࡱࡸࡸࠬᦲ"),
  bstack1lll11l_opy_ (u"࠭࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࡔࡧࡵࡺ࡮ࡩࡥࡴࡇࡱࡥࡧࡲࡥࡥࠩᦳ"), bstack1lll11l_opy_ (u"ࠧ࡭ࡱࡦࡥࡹ࡯࡯࡯ࡕࡨࡶࡻ࡯ࡣࡦࡵࡄࡹࡹ࡮࡯ࡳ࡫ࡽࡩࡩ࠭ᦴ"),
  bstack1lll11l_opy_ (u"ࠨࡣࡸࡸࡴࡇࡣࡤࡧࡳࡸࡆࡲࡥࡳࡶࡶࠫᦵ"), bstack1lll11l_opy_ (u"ࠩࡤࡹࡹࡵࡄࡪࡵࡰ࡭ࡸࡹࡁ࡭ࡧࡵࡸࡸ࠭ᦶ"),
  bstack1lll11l_opy_ (u"ࠪࡲࡦࡺࡩࡷࡧࡌࡲࡸࡺࡲࡶ࡯ࡨࡲࡹࡹࡌࡪࡤࠪᦷ"),
  bstack1lll11l_opy_ (u"ࠫࡳࡧࡴࡪࡸࡨ࡛ࡪࡨࡔࡢࡲࠪᦸ"),
  bstack1lll11l_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࡎࡴࡩࡵ࡫ࡤࡰ࡚ࡸ࡬ࠨᦹ"), bstack1lll11l_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮ࡇ࡬࡭ࡱࡺࡔࡴࡶࡵࡱࡵࠪᦺ"), bstack1lll11l_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࡉࡨࡰࡲࡶࡪࡌࡲࡢࡷࡧ࡛ࡦࡸ࡮ࡪࡰࡪࠫᦻ"), bstack1lll11l_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࡐࡲࡨࡲࡑ࡯࡮࡬ࡵࡌࡲࡇࡧࡣ࡬ࡩࡵࡳࡺࡴࡤࠨᦼ"),
  bstack1lll11l_opy_ (u"ࠩ࡮ࡩࡪࡶࡋࡦࡻࡆ࡬ࡦ࡯࡮ࡴࠩᦽ"),
  bstack1lll11l_opy_ (u"ࠪࡰࡴࡩࡡ࡭࡫ࡽࡥࡧࡲࡥࡔࡶࡵ࡭ࡳ࡭ࡳࡅ࡫ࡵࠫᦾ"),
  bstack1lll11l_opy_ (u"ࠫࡵࡸ࡯ࡤࡧࡶࡷࡆࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᦿ"),
  bstack1lll11l_opy_ (u"ࠬ࡯࡮ࡵࡧࡵࡏࡪࡿࡄࡦ࡮ࡤࡽࠬᧀ"),
  bstack1lll11l_opy_ (u"࠭ࡳࡩࡱࡺࡍࡔ࡙ࡌࡰࡩࠪᧁ"),
  bstack1lll11l_opy_ (u"ࠧࡴࡧࡱࡨࡐ࡫ࡹࡔࡶࡵࡥࡹ࡫ࡧࡺࠩᧂ"),
  bstack1lll11l_opy_ (u"ࠨࡹࡨࡦࡰ࡯ࡴࡓࡧࡶࡴࡴࡴࡳࡦࡖ࡬ࡱࡪࡵࡵࡵࠩᧃ"), bstack1lll11l_opy_ (u"ࠩࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹ࡝ࡡࡪࡶࡗ࡭ࡲ࡫࡯ࡶࡶࠪᧄ"),
  bstack1lll11l_opy_ (u"ࠪࡶࡪࡳ࡯ࡵࡧࡇࡩࡧࡻࡧࡑࡴࡲࡼࡾ࠭ᧅ"),
  bstack1lll11l_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡅࡸࡿ࡮ࡤࡇࡻࡩࡨࡻࡴࡦࡈࡵࡳࡲࡎࡴࡵࡲࡶࠫᧆ"),
  bstack1lll11l_opy_ (u"ࠬࡹ࡫ࡪࡲࡏࡳ࡬ࡉࡡࡱࡶࡸࡶࡪ࠭ᧇ"),
  bstack1lll11l_opy_ (u"࠭ࡷࡦࡤ࡮࡭ࡹࡊࡥࡣࡷࡪࡔࡷࡵࡸࡺࡒࡲࡶࡹ࠭ᧈ"),
  bstack1lll11l_opy_ (u"ࠧࡧࡷ࡯ࡰࡈࡵ࡮ࡵࡧࡻࡸࡑ࡯ࡳࡵࠩᧉ"),
  bstack1lll11l_opy_ (u"ࠨࡹࡤ࡭ࡹࡌ࡯ࡳࡃࡳࡴࡘࡩࡲࡪࡲࡷࠫ᧊"),
  bstack1lll11l_opy_ (u"ࠩࡺࡩࡧࡼࡩࡦࡹࡆࡳࡳࡴࡥࡤࡶࡕࡩࡹࡸࡩࡦࡵࠪ᧋"),
  bstack1lll11l_opy_ (u"ࠪࡥࡵࡶࡎࡢ࡯ࡨࠫ᧌"),
  bstack1lll11l_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡗࡘࡒࡃࡦࡴࡷࠫ᧍"),
  bstack1lll11l_opy_ (u"ࠬࡺࡡࡱ࡙࡬ࡸ࡭࡙ࡨࡰࡴࡷࡔࡷ࡫ࡳࡴࡆࡸࡶࡦࡺࡩࡰࡰࠪ᧎"),
  bstack1lll11l_opy_ (u"࠭ࡳࡤࡣ࡯ࡩࡋࡧࡣࡵࡱࡵࠫ᧏"),
  bstack1lll11l_opy_ (u"ࠧࡸࡦࡤࡐࡴࡩࡡ࡭ࡒࡲࡶࡹ࠭᧐"),
  bstack1lll11l_opy_ (u"ࠨࡵ࡫ࡳࡼ࡞ࡣࡰࡦࡨࡐࡴ࡭ࠧ᧑"),
  bstack1lll11l_opy_ (u"ࠩ࡬ࡳࡸࡏ࡮ࡴࡶࡤࡰࡱࡖࡡࡶࡵࡨࠫ᧒"),
  bstack1lll11l_opy_ (u"ࠪࡼࡨࡵࡤࡦࡅࡲࡲ࡫࡯ࡧࡇ࡫࡯ࡩࠬ᧓"),
  bstack1lll11l_opy_ (u"ࠫࡰ࡫ࡹࡤࡪࡤ࡭ࡳࡖࡡࡴࡵࡺࡳࡷࡪࠧ᧔"),
  bstack1lll11l_opy_ (u"ࠬࡻࡳࡦࡒࡵࡩࡧࡻࡩ࡭ࡶ࡚ࡈࡆ࠭᧕"),
  bstack1lll11l_opy_ (u"࠭ࡰࡳࡧࡹࡩࡳࡺࡗࡅࡃࡄࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠧ᧖"),
  bstack1lll11l_opy_ (u"ࠧࡸࡧࡥࡈࡷ࡯ࡶࡦࡴࡄ࡫ࡪࡴࡴࡖࡴ࡯ࠫ᧗"),
  bstack1lll11l_opy_ (u"ࠨ࡭ࡨࡽࡨ࡮ࡡࡪࡰࡓࡥࡹ࡮ࠧ᧘"),
  bstack1lll11l_opy_ (u"ࠩࡸࡷࡪࡔࡥࡸ࡙ࡇࡅࠬ᧙"),
  bstack1lll11l_opy_ (u"ࠪࡻࡩࡧࡌࡢࡷࡱࡧ࡭࡚ࡩ࡮ࡧࡲࡹࡹ࠭᧚"), bstack1lll11l_opy_ (u"ࠫࡼࡪࡡࡄࡱࡱࡲࡪࡩࡴࡪࡱࡱࡘ࡮ࡳࡥࡰࡷࡷࠫ᧛"),
  bstack1lll11l_opy_ (u"ࠬࡾࡣࡰࡦࡨࡓࡷ࡭ࡉࡥࠩ᧜"), bstack1lll11l_opy_ (u"࠭ࡸࡤࡱࡧࡩࡘ࡯ࡧ࡯࡫ࡱ࡫ࡎࡪࠧ᧝"),
  bstack1lll11l_opy_ (u"ࠧࡶࡲࡧࡥࡹ࡫ࡤࡘࡆࡄࡆࡺࡴࡤ࡭ࡧࡌࡨࠬ᧞"),
  bstack1lll11l_opy_ (u"ࠨࡴࡨࡷࡪࡺࡏ࡯ࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡷࡺࡏ࡯࡮ࡼࠫ᧟"),
  bstack1lll11l_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡗ࡭ࡲ࡫࡯ࡶࡶࡶࠫ᧠"),
  bstack1lll11l_opy_ (u"ࠪࡻࡩࡧࡓࡵࡣࡵࡸࡺࡶࡒࡦࡶࡵ࡭ࡪࡹࠧ᧡"), bstack1lll11l_opy_ (u"ࠫࡼࡪࡡࡔࡶࡤࡶࡹࡻࡰࡓࡧࡷࡶࡾࡏ࡮ࡵࡧࡵࡺࡦࡲࠧ᧢"),
  bstack1lll11l_opy_ (u"ࠬࡩ࡯࡯ࡰࡨࡧࡹࡎࡡࡳࡦࡺࡥࡷ࡫ࡋࡦࡻࡥࡳࡦࡸࡤࠨ᧣"),
  bstack1lll11l_opy_ (u"࠭࡭ࡢࡺࡗࡽࡵ࡯࡮ࡨࡈࡵࡩࡶࡻࡥ࡯ࡥࡼࠫ᧤"),
  bstack1lll11l_opy_ (u"ࠧࡴ࡫ࡰࡴࡱ࡫ࡉࡴࡘ࡬ࡷ࡮ࡨ࡬ࡦࡅ࡫ࡩࡨࡱࠧ᧥"),
  bstack1lll11l_opy_ (u"ࠨࡷࡶࡩࡈࡧࡲࡵࡪࡤ࡫ࡪ࡙ࡳ࡭ࠩ᧦"),
  bstack1lll11l_opy_ (u"ࠩࡶ࡬ࡴࡻ࡬ࡥࡗࡶࡩࡘ࡯࡮ࡨ࡮ࡨࡸࡴࡴࡔࡦࡵࡷࡑࡦࡴࡡࡨࡧࡵࠫ᧧"),
  bstack1lll11l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡋ࡚ࡈࡕ࠭᧨"),
  bstack1lll11l_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡗࡳࡺࡩࡨࡊࡦࡈࡲࡷࡵ࡬࡭ࠩ᧩"),
  bstack1lll11l_opy_ (u"ࠬ࡯ࡧ࡯ࡱࡵࡩࡍ࡯ࡤࡥࡧࡱࡅࡵ࡯ࡐࡰ࡮࡬ࡧࡾࡋࡲࡳࡱࡵࠫ᧪"),
  bstack1lll11l_opy_ (u"࠭࡭ࡰࡥ࡮ࡐࡴࡩࡡࡵ࡫ࡲࡲࡆࡶࡰࠨ᧫"),
  bstack1lll11l_opy_ (u"ࠧ࡭ࡱࡪࡧࡦࡺࡆࡰࡴࡰࡥࡹ࠭᧬"), bstack1lll11l_opy_ (u"ࠨ࡮ࡲ࡫ࡨࡧࡴࡇ࡫࡯ࡸࡪࡸࡓࡱࡧࡦࡷࠬ᧭"),
  bstack1lll11l_opy_ (u"ࠩࡤࡰࡱࡵࡷࡅࡧ࡯ࡥࡾࡇࡤࡣࠩ᧮"),
  bstack1lll11l_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡍࡩࡒ࡯ࡤࡣࡷࡳࡷࡇࡵࡵࡱࡦࡳࡲࡶ࡬ࡦࡶ࡬ࡳࡳ࠭᧯")
]
bstack1l11llll11_opy_ = bstack1lll11l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠯ࡦࡰࡴࡻࡤ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧ࠲ࡹࡵࡲ࡯ࡢࡦࠪ᧰")
bstack1l1l1l1l1l_opy_ = [bstack1lll11l_opy_ (u"ࠬ࠴ࡡࡱ࡭ࠪ᧱"), bstack1lll11l_opy_ (u"࠭࠮ࡢࡣࡥࠫ᧲"), bstack1lll11l_opy_ (u"ࠧ࠯࡫ࡳࡥࠬ᧳")]
bstack1111l1lll_opy_ = [bstack1lll11l_opy_ (u"ࠨ࡫ࡧࠫ᧴"), bstack1lll11l_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ᧵"), bstack1lll11l_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭᧶"), bstack1lll11l_opy_ (u"ࠫࡸ࡮ࡡࡳࡧࡤࡦࡱ࡫࡟ࡪࡦࠪ᧷")]
bstack111l1l1ll_opy_ = {
  bstack1lll11l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ᧸"): bstack1lll11l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ᧹"),
  bstack1lll11l_opy_ (u"ࠧࡧ࡫ࡵࡩ࡫ࡵࡸࡐࡲࡷ࡭ࡴࡴࡳࠨ᧺"): bstack1lll11l_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭᧻"),
  bstack1lll11l_opy_ (u"ࠩࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ᧼"): bstack1lll11l_opy_ (u"ࠪࡱࡸࡀࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫ᧽"),
  bstack1lll11l_opy_ (u"ࠫ࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ᧾"): bstack1lll11l_opy_ (u"ࠬࡹࡥ࠻࡫ࡨࡓࡵࡺࡩࡰࡰࡶࠫ᧿"),
  bstack1lll11l_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮ࡕࡰࡵ࡫ࡲࡲࡸ࠭ᨀ"): bstack1lll11l_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨᨁ")
}
bstack1l1l1l1l1_opy_ = [
  bstack1lll11l_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᨂ"),
  bstack1lll11l_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧᨃ"),
  bstack1lll11l_opy_ (u"ࠪࡱࡸࡀࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫᨄ"),
  bstack1lll11l_opy_ (u"ࠫࡸ࡫࠺ࡪࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᨅ"),
  bstack1lll11l_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᨆ"),
]
bstack1l1lll1l1_opy_ = bstack1l1ll11ll1_opy_ + bstack11l1l11l111_opy_ + bstack11lll1l1l_opy_
bstack1lllll1111_opy_ = [
  bstack1lll11l_opy_ (u"࠭࡞࡭ࡱࡦࡥࡱ࡮࡯ࡴࡶࠧࠫᨇ"),
  bstack1lll11l_opy_ (u"ࠧ࡟ࡤࡶ࠱ࡱࡵࡣࡢ࡮࠱ࡧࡴࡳࠤࠨᨈ"),
  bstack1lll11l_opy_ (u"ࠨࡠ࠴࠶࠼࠴ࠧᨉ"),
  bstack1lll11l_opy_ (u"ࠩࡡ࠵࠵࠴ࠧᨊ"),
  bstack1lll11l_opy_ (u"ࠪࡢ࠶࠽࠲࠯࠳࡞࠺࠲࠿࡝࠯ࠩᨋ"),
  bstack1lll11l_opy_ (u"ࠫࡣ࠷࠷࠳࠰࠵࡟࠵࠳࠹࡞࠰ࠪᨌ"),
  bstack1lll11l_opy_ (u"ࠬࡤ࠱࠸࠴࠱࠷ࡠ࠶࠭࠲࡟࠱ࠫᨍ"),
  bstack1lll11l_opy_ (u"࠭࡞࠲࠻࠵࠲࠶࠼࠸࠯ࠩᨎ")
]
bstack11l1l111111_opy_ = bstack1lll11l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨᨏ")
bstack1l1111111l_opy_ = bstack1lll11l_opy_ (u"ࠨࡵࡧ࡯࠴ࡼ࠱࠰ࡧࡹࡩࡳࡺࠧᨐ")
bstack11l111l11l_opy_ = [ bstack1lll11l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫᨑ") ]
bstack11l1lllll_opy_ = [ bstack1lll11l_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩᨒ") ]
bstack11l1l1l1ll_opy_ = [bstack1lll11l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨᨓ")]
bstack11l11l1l11_opy_ = [ bstack1lll11l_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬᨔ") ]
bstack11llll1l1l_opy_ = bstack1lll11l_opy_ (u"࠭ࡓࡅࡍࡖࡩࡹࡻࡰࠨᨕ")
bstack11l11ll1l_opy_ = bstack1lll11l_opy_ (u"ࠧࡔࡆࡎࡘࡪࡹࡴࡂࡶࡷࡩࡲࡶࡴࡦࡦࠪᨖ")
bstack1lll111ll1_opy_ = bstack1lll11l_opy_ (u"ࠨࡕࡇࡏ࡙࡫ࡳࡵࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࠬᨗ")
bstack111l1l111_opy_ = bstack1lll11l_opy_ (u"ࠩ࠷࠲࠵࠴࠰ࠨᨘ")
bstack11ll11l1l1_opy_ = [
  bstack1lll11l_opy_ (u"ࠪࡉࡗࡘ࡟ࡇࡃࡌࡐࡊࡊࠧᨙ"),
  bstack1lll11l_opy_ (u"ࠫࡊࡘࡒࡠࡖࡌࡑࡊࡊ࡟ࡐࡗࡗࠫᨚ"),
  bstack1lll11l_opy_ (u"ࠬࡋࡒࡓࡡࡅࡐࡔࡉࡋࡆࡆࡢࡆ࡞ࡥࡃࡍࡋࡈࡒ࡙࠭ᨛ"),
  bstack1lll11l_opy_ (u"࠭ࡅࡓࡔࡢࡒࡊ࡚ࡗࡐࡔࡎࡣࡈࡎࡁࡏࡉࡈࡈࠬ᨜"),
  bstack1lll11l_opy_ (u"ࠧࡆࡔࡕࡣࡘࡕࡃࡌࡇࡗࡣࡓࡕࡔࡠࡅࡒࡒࡓࡋࡃࡕࡇࡇࠫ᨝"),
  bstack1lll11l_opy_ (u"ࠨࡇࡕࡖࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡆࡐࡔ࡙ࡅࡅࠩ᨞"),
  bstack1lll11l_opy_ (u"ࠩࡈࡖࡗࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡖࡊ࡙ࡅࡕࠩ᨟"),
  bstack1lll11l_opy_ (u"ࠪࡉࡗࡘ࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣࡗࡋࡆࡖࡕࡈࡈࠬᨠ"),
  bstack1lll11l_opy_ (u"ࠫࡊࡘࡒࡠࡅࡒࡒࡓࡋࡃࡕࡋࡒࡒࡤࡇࡂࡐࡔࡗࡉࡉ࠭ᨡ"),
  bstack1lll11l_opy_ (u"ࠬࡋࡒࡓࡡࡆࡓࡓࡔࡅࡄࡖࡌࡓࡓࡥࡆࡂࡋࡏࡉࡉ࠭ᨢ"),
  bstack1lll11l_opy_ (u"࠭ࡅࡓࡔࡢࡒࡆࡓࡅࡠࡐࡒࡘࡤࡘࡅࡔࡑࡏ࡚ࡊࡊࠧᨣ"),
  bstack1lll11l_opy_ (u"ࠧࡆࡔࡕࡣࡆࡊࡄࡓࡇࡖࡗࡤࡏࡎࡗࡃࡏࡍࡉ࠭ᨤ"),
  bstack1lll11l_opy_ (u"ࠨࡇࡕࡖࡤࡇࡄࡅࡔࡈࡗࡘࡥࡕࡏࡔࡈࡅࡈࡎࡁࡃࡎࡈࠫᨥ"),
  bstack1lll11l_opy_ (u"ࠩࡈࡖࡗࡥࡔࡖࡐࡑࡉࡑࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡊࡆࡏࡌࡆࡆࠪᨦ"),
  bstack1lll11l_opy_ (u"ࠪࡉࡗࡘ࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣ࡙ࡏࡍࡆࡆࡢࡓ࡚࡚ࠧᨧ"),
  bstack1lll11l_opy_ (u"ࠫࡊࡘࡒࡠࡕࡒࡇࡐ࡙࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣࡋࡇࡉࡍࡇࡇࠫᨨ"),
  bstack1lll11l_opy_ (u"ࠬࡋࡒࡓࡡࡖࡓࡈࡑࡓࡠࡅࡒࡒࡓࡋࡃࡕࡋࡒࡒࡤࡎࡏࡔࡖࡢ࡙ࡓࡘࡅࡂࡅࡋࡅࡇࡒࡅࠨᨩ"),
  bstack1lll11l_opy_ (u"࠭ࡅࡓࡔࡢࡔࡗࡕࡘ࡚ࡡࡆࡓࡓࡔࡅࡄࡖࡌࡓࡓࡥࡆࡂࡋࡏࡉࡉ࠭ᨪ"),
  bstack1lll11l_opy_ (u"ࠧࡆࡔࡕࡣࡓࡇࡍࡆࡡࡑࡓ࡙ࡥࡒࡆࡕࡒࡐ࡛ࡋࡄࠨᨫ"),
  bstack1lll11l_opy_ (u"ࠨࡇࡕࡖࡤࡔࡁࡎࡇࡢࡖࡊ࡙ࡏࡍࡗࡗࡍࡔࡔ࡟ࡇࡃࡌࡐࡊࡊࠧᨬ"),
  bstack1lll11l_opy_ (u"ࠩࡈࡖࡗࡥࡍࡂࡐࡇࡅ࡙ࡕࡒ࡚ࡡࡓࡖࡔ࡞࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠࡈࡄࡍࡑࡋࡄࠨᨭ"),
]
bstack1l1l11l1l_opy_ = bstack1lll11l_opy_ (u"ࠪ࠲࠴ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠱ࡦࡸࡴࡪࡨࡤࡧࡹࡹ࠯ࠨᨮ")
bstack1111ll1l1_opy_ = os.path.join(os.path.expanduser(bstack1lll11l_opy_ (u"ࠫࢃ࠭ᨯ")), bstack1lll11l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᨰ"), bstack1lll11l_opy_ (u"࠭࠮ࡣࡵࡷࡥࡨࡱ࠭ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬᨱ"))
bstack11l11l11lll_opy_ = bstack1lll11l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡦࡶࡩࠨᨲ")
bstack11l1l1111l1_opy_ = [ bstack1lll11l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨᨳ"), bstack1lll11l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨᨴ"), bstack1lll11l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩᨵ"), bstack1lll11l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫᨶ")]
bstack1l111lll1_opy_ = [ bstack1lll11l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬᨷ"), bstack1lll11l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬᨸ"), bstack1lll11l_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ᨹ"), bstack1lll11l_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨᨺ") ]
bstack11lllll11l_opy_ = [ bstack1lll11l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨᨻ") ]
bstack11l11llll11_opy_ = [ bstack1lll11l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪᨼ") ]
bstack1l11lll11l_opy_ = 360
bstack11ll11l1l11_opy_ = bstack1lll11l_opy_ (u"ࠦࡦࡶࡰ࠮ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠦᨽ")
bstack11l11l1l1l1_opy_ = bstack1lll11l_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫࠯ࡢࡲ࡬࠳ࡻ࠷࠯ࡪࡵࡶࡹࡪࡹࠢᨾ")
bstack11l11ll1l11_opy_ = bstack1lll11l_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡥ࠰ࡣࡳ࡭࠴ࡼ࠱࠰࡫ࡶࡷࡺ࡫ࡳ࠮ࡵࡸࡱࡲࡧࡲࡺࠤᨿ")
bstack11l11lll1ll_opy_ = bstack1lll11l_opy_ (u"ࠢࡂࡲࡳࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡶࡨࡷࡹࡹࠠࡢࡴࡨࠤࡸࡻࡰࡱࡱࡵࡸࡪࡪࠠࡰࡰࠣࡓࡘࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࠦࡵࠣࡥࡳࡪࠠࡢࡤࡲࡺࡪࠦࡦࡰࡴࠣࡅࡳࡪࡲࡰ࡫ࡧࠤࡩ࡫ࡶࡪࡥࡨࡷ࠳ࠨᩀ")
bstack11l1l11ll11_opy_ = bstack1lll11l_opy_ (u"ࠣ࠳࠴࠲࠵ࠨᩁ")
bstack1lll111l_opy_ = {
  bstack1lll11l_opy_ (u"ࠩࡓࡅࡘ࡙ࠧᩂ"): bstack1lll11l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᩃ"),
  bstack1lll11l_opy_ (u"ࠫࡋࡇࡉࡍࠩᩄ"): bstack1lll11l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᩅ"),
  bstack1lll11l_opy_ (u"࠭ࡓࡌࡋࡓࠫᩆ"): bstack1lll11l_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᩇ")
}
bstack1111ll11ll_opy_ = [
  bstack1lll11l_opy_ (u"ࠣࡩࡨࡸࠧᩈ"),
  bstack1lll11l_opy_ (u"ࠤࡪࡳࡇࡧࡣ࡬ࠤᩉ"),
  bstack1lll11l_opy_ (u"ࠥ࡫ࡴࡌ࡯ࡳࡹࡤࡶࡩࠨᩊ"),
  bstack1lll11l_opy_ (u"ࠦࡷ࡫ࡦࡳࡧࡶ࡬ࠧᩋ"),
  bstack1lll11l_opy_ (u"ࠧࡩ࡬ࡪࡥ࡮ࡉࡱ࡫࡭ࡦࡰࡷࠦᩌ"),
  bstack1lll11l_opy_ (u"ࠨࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠥᩍ"),
  bstack1lll11l_opy_ (u"ࠢࡴࡷࡥࡱ࡮ࡺࡅ࡭ࡧࡰࡩࡳࡺࠢᩎ"),
  bstack1lll11l_opy_ (u"ࠣࡵࡨࡲࡩࡑࡥࡺࡵࡗࡳࡊࡲࡥ࡮ࡧࡱࡸࠧᩏ"),
  bstack1lll11l_opy_ (u"ࠤࡶࡩࡳࡪࡋࡦࡻࡶࡘࡴࡇࡣࡵ࡫ࡹࡩࡊࡲࡥ࡮ࡧࡱࡸࠧᩐ"),
  bstack1lll11l_opy_ (u"ࠥࡧࡱ࡫ࡡࡳࡇ࡯ࡩࡲ࡫࡮ࡵࠤᩑ"),
  bstack1lll11l_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࡷࠧᩒ"),
  bstack1lll11l_opy_ (u"ࠧ࡫ࡸࡦࡥࡸࡸࡪ࡙ࡣࡳ࡫ࡳࡸࠧᩓ"),
  bstack1lll11l_opy_ (u"ࠨࡥࡹࡧࡦࡹࡹ࡫ࡁࡴࡻࡱࡧࡘࡩࡲࡪࡲࡷࠦᩔ"),
  bstack1lll11l_opy_ (u"ࠢࡤ࡮ࡲࡷࡪࠨᩕ"),
  bstack1lll11l_opy_ (u"ࠣࡳࡸ࡭ࡹࠨᩖ"),
  bstack1lll11l_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡗࡳࡺࡩࡨࡂࡥࡷ࡭ࡴࡴࠢᩗ"),
  bstack1lll11l_opy_ (u"ࠥࡴࡪࡸࡦࡰࡴࡰࡑࡺࡲࡴࡪࡖࡲࡹࡨ࡮ࠢᩘ"),
  bstack1lll11l_opy_ (u"ࠦࡸ࡮ࡡ࡬ࡧࠥᩙ"),
  bstack1lll11l_opy_ (u"ࠧࡩ࡬ࡰࡵࡨࡅࡵࡶࠢᩚ")
]
bstack11l1l11l1ll_opy_ = [
  bstack1lll11l_opy_ (u"ࠨࡣ࡭࡫ࡦ࡯ࠧᩛ"),
  bstack1lll11l_opy_ (u"ࠢࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠦᩜ"),
  bstack1lll11l_opy_ (u"ࠣࡣࡸࡸࡴࠨᩝ"),
  bstack1lll11l_opy_ (u"ࠤࡰࡥࡳࡻࡡ࡭ࠤᩞ"),
  bstack1lll11l_opy_ (u"ࠥࡸࡪࡹࡴࡤࡣࡶࡩࠧ᩟")
]
bstack11111l1lll_opy_ = {
  bstack1lll11l_opy_ (u"ࠦࡨࡲࡩࡤ࡭᩠ࠥ"): [bstack1lll11l_opy_ (u"ࠧࡩ࡬ࡪࡥ࡮ࡉࡱ࡫࡭ࡦࡰࡷࠦᩡ")],
  bstack1lll11l_opy_ (u"ࠨࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠥᩢ"): [bstack1lll11l_opy_ (u"ࠢࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠦᩣ")],
  bstack1lll11l_opy_ (u"ࠣࡣࡸࡸࡴࠨᩤ"): [bstack1lll11l_opy_ (u"ࠤࡶࡩࡳࡪࡋࡦࡻࡶࡘࡴࡋ࡬ࡦ࡯ࡨࡲࡹࠨᩥ"), bstack1lll11l_opy_ (u"ࠥࡷࡪࡴࡤࡌࡧࡼࡷ࡙ࡵࡁࡤࡶ࡬ࡺࡪࡋ࡬ࡦ࡯ࡨࡲࡹࠨᩦ"), bstack1lll11l_opy_ (u"ࠦࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣᩧ"), bstack1lll11l_opy_ (u"ࠧࡩ࡬ࡪࡥ࡮ࡉࡱ࡫࡭ࡦࡰࡷࠦᩨ")],
  bstack1lll11l_opy_ (u"ࠨ࡭ࡢࡰࡸࡥࡱࠨᩩ"): [bstack1lll11l_opy_ (u"ࠢ࡮ࡣࡱࡹࡦࡲࠢᩪ")],
  bstack1lll11l_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥᩫ"): [bstack1lll11l_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦᩬ")],
}
bstack11l1l11ll1l_opy_ = {
  bstack1lll11l_opy_ (u"ࠥࡧࡱ࡯ࡣ࡬ࡇ࡯ࡩࡲ࡫࡮ࡵࠤᩭ"): bstack1lll11l_opy_ (u"ࠦࡨࡲࡩࡤ࡭ࠥᩮ"),
  bstack1lll11l_opy_ (u"ࠧࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠤᩯ"): bstack1lll11l_opy_ (u"ࠨࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠥᩰ"),
  bstack1lll11l_opy_ (u"ࠢࡴࡧࡱࡨࡐ࡫ࡹࡴࡖࡲࡉࡱ࡫࡭ࡦࡰࡷࠦᩱ"): bstack1lll11l_opy_ (u"ࠣࡵࡨࡲࡩࡑࡥࡺࡵࠥᩲ"),
  bstack1lll11l_opy_ (u"ࠤࡶࡩࡳࡪࡋࡦࡻࡶࡘࡴࡇࡣࡵ࡫ࡹࡩࡊࡲࡥ࡮ࡧࡱࡸࠧᩳ"): bstack1lll11l_opy_ (u"ࠥࡷࡪࡴࡤࡌࡧࡼࡷࠧᩴ"),
  bstack1lll11l_opy_ (u"ࠦࡹ࡫ࡳࡵࡥࡤࡷࡪࠨ᩵"): bstack1lll11l_opy_ (u"ࠧࡺࡥࡴࡶࡦࡥࡸ࡫ࠢ᩶")
}
bstack1ll11lll_opy_ = {
  bstack1lll11l_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡁࡍࡎࠪ᩷"): bstack1lll11l_opy_ (u"ࠧࡔࡷ࡬ࡸࡪࠦࡓࡦࡶࡸࡴࠬ᩸"),
  bstack1lll11l_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫ᩹"): bstack1lll11l_opy_ (u"ࠩࡖࡹ࡮ࡺࡥࠡࡖࡨࡥࡷࡪ࡯ࡸࡰࠪ᩺"),
  bstack1lll11l_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨ᩻"): bstack1lll11l_opy_ (u"࡙ࠫ࡫ࡳࡵࠢࡖࡩࡹࡻࡰࠨ᩼"),
  bstack1lll11l_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩ᩽"): bstack1lll11l_opy_ (u"࠭ࡔࡦࡵࡷࠤ࡙࡫ࡡࡳࡦࡲࡻࡳ࠭᩾")
}
bstack11l11lllll1_opy_ = 65536
bstack11l11ll11ll_opy_ = bstack1lll11l_opy_ (u"ࠧ࠯࠰࠱࡟࡙ࡘࡕࡏࡅࡄࡘࡊࡊ࡝ࠨ᩿")
bstack11l11l11l1l_opy_ = [
      bstack1lll11l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ᪀"), bstack1lll11l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ᪁"), bstack1lll11l_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭᪂"), bstack1lll11l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨ᪃"), bstack1lll11l_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱ࡛ࡧࡲࡪࡣࡥࡰࡪࡹࠧ᪄"),
      bstack1lll11l_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡚ࡹࡥࡳࠩ᪅"), bstack1lll11l_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖࡡࡴࡵࠪ᪆"), bstack1lll11l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡐࡳࡱࡻࡽ࡚ࡹࡥࡳࠩ᪇"), bstack1lll11l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡑࡴࡲࡼࡾࡖࡡࡴࡵࠪ᪈"),
      bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ᪉"), bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭᪊"), bstack1lll11l_opy_ (u"ࠬࡧࡵࡵࡪࡗࡳࡰ࡫࡮ࠨ᪋")
    ]
bstack11l11l1l11l_opy_= {
  bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ᪌"): bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ᪍"),
  bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ᪎"): bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭᪏"),
  bstack1lll11l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᪐"): bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ᪑"),
  bstack1lll11l_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ᪒"): bstack1lll11l_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭᪓"),
  bstack1lll11l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ᪔"): bstack1lll11l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ᪕"),
  bstack1lll11l_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫ᪖"): bstack1lll11l_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬ᪗"),
  bstack1lll11l_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧ᪘"): bstack1lll11l_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ᪙"),
  bstack1lll11l_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ᪚"): bstack1lll11l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ᪛"),
  bstack1lll11l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ᪜"): bstack1lll11l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ᪝"),
  bstack1lll11l_opy_ (u"ࠪࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠨ᪞"): bstack1lll11l_opy_ (u"ࠫࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᪟"),
  bstack1lll11l_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ᪠"): bstack1lll11l_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ᪡"),
  bstack1lll11l_opy_ (u"ࠧࡵࡧࡶࡸࡗ࡫ࡰࡰࡴࡷ࡭ࡳ࡭ࠧ᪢"): bstack1lll11l_opy_ (u"ࠨࡶࡨࡷࡹࡘࡥࡱࡱࡵࡸ࡮ࡴࡧࠨ᪣"),
  bstack1lll11l_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭᪤"): bstack1lll11l_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ᪥"),
  bstack1lll11l_opy_ (u"ࠫࡹ࡫ࡳࡵࡔࡨࡴࡴࡸࡴࡪࡰࡪࡓࡵࡺࡩࡰࡰࡶࠫ᪦"): bstack1lll11l_opy_ (u"ࠬࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࡔࡶࡴࡪࡱࡱࡷࠬᪧ"),
  bstack1lll11l_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠨ᪨"): bstack1lll11l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠩ᪩"),
  bstack1lll11l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ᪪"): bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ᪫"),
  bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ᪬"): bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭᪭"),
  bstack1lll11l_opy_ (u"ࠬࡸࡥࡳࡷࡱࡘࡪࡹࡴࡴࠩ᪮"): bstack1lll11l_opy_ (u"࠭ࡲࡦࡴࡸࡲ࡙࡫ࡳࡵࡵࠪ᪯"),
  bstack1lll11l_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭᪰"): bstack1lll11l_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧ᪱"),
  bstack1lll11l_opy_ (u"ࠩࡳࡩࡷࡩࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ᪲"): bstack1lll11l_opy_ (u"ࠪࡴࡪࡸࡣࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᪳"),
  bstack1lll11l_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡆࡥࡵࡺࡵࡳࡧࡐࡳࡩ࡫ࠧ᪴"): bstack1lll11l_opy_ (u"ࠬࡶࡥࡳࡥࡼࡇࡦࡶࡴࡶࡴࡨࡑࡴࡪࡥࠨ᪵"),
  bstack1lll11l_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁࡶࡶࡲࡇࡦࡶࡴࡶࡴࡨࡐࡴ࡭ࡳࠨ᪶"): bstack1lll11l_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴ᪷ࠩ"),
  bstack1lll11l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ᪸"): bstack1lll11l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺ᪹ࠩ"),
  bstack1lll11l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵ᪺ࠪ"): bstack1lll11l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ᪻"),
  bstack1lll11l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ᪼"): bstack1lll11l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧ᪽ࠪ"),
  bstack1lll11l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࡓࡵࡺࡩࡰࡰࡶࠫ᪾"): bstack1lll11l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࡔࡶࡴࡪࡱࡱࡷᪿࠬ"),
  bstack1lll11l_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸᫀ࠭"): bstack1lll11l_opy_ (u"ࠪࡸࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡏࡱࡶ࡬ࡳࡳࡹࠧ᫁"),
  bstack1lll11l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡖࡩࡹࡺࡩ࡯ࡩࡶࠫ᫂"): bstack1lll11l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷ᫃ࠬ")
}
bstack11l11l1ll1l_opy_ = [bstack1lll11l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ᫄࠭"), bstack1lll11l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭᫅")]
bstack1ll1llll11_opy_ = (bstack1lll11l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣ᫆"),)
bstack11l11ll1111_opy_ = bstack1lll11l_opy_ (u"ࠩࡶࡨࡰ࠵ࡶ࠲࠱ࡸࡴࡩࡧࡴࡦࡡࡦࡰ࡮࠭᫇")
bstack1l1ll11111_opy_ = bstack1lll11l_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡦࡶࡩ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠳ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧ࠲ࡺ࠶࠵ࡧࡳ࡫ࡧࡷ࠴ࠨ᫈")
bstack11111111l_opy_ = bstack1lll11l_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴࡭ࡲࡪࡦ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡤࡢࡵ࡫ࡦࡴࡧࡲࡥ࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࠥ᫉")
bstack1111ll1ll1_opy_ = bstack1lll11l_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡱ࡫࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡡࡶࡶࡲࡱࡦࡺࡥ࠮ࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩ࠴ࡼ࠱࠰ࡤࡸ࡭ࡱࡪࡳ࠯࡬ࡶࡳࡳࠨ᫊")
class EVENTS(Enum):
  bstack11l11llll1l_opy_ = bstack1lll11l_opy_ (u"࠭ࡳࡥ࡭࠽ࡳ࠶࠷ࡹ࠻ࡲࡵ࡭ࡳࡺ࠭ࡣࡷ࡬ࡰࡩࡲࡩ࡯࡭ࠪ᫋")
  bstack11l1ll11ll_opy_ = bstack1lll11l_opy_ (u"ࠧࡴࡦ࡮࠾ࡨࡲࡥࡢࡰࡸࡴࠬᫌ") # final bstack11l1l111l1l_opy_
  bstack11l1l111l11_opy_ = bstack1lll11l_opy_ (u"ࠨࡵࡧ࡯࠿ࡹࡥ࡯ࡦ࡯ࡳ࡬ࡹࠧᫍ")
  bstack1111ll1lll_opy_ = bstack1lll11l_opy_ (u"ࠩࡶࡨࡰࡀࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧ࠽ࡴࡷ࡯࡮ࡵ࠯ࡥࡹ࡮ࡲࡤ࡭࡫ࡱ࡯ࠬᫎ") #shift post bstack11l1l11lll1_opy_
  bstack11ll1l1l11_opy_ = bstack1lll11l_opy_ (u"ࠪࡷࡩࡱ࠺ࡢࡷࡷࡳࡲࡧࡴࡦ࠼ࡳࡶ࡮ࡴࡴ࠮ࡤࡸ࡭ࡱࡪ࡬ࡪࡰ࡮ࠫ᫏") #shift post bstack11l1l11lll1_opy_
  bstack11l11lll11l_opy_ = bstack1lll11l_opy_ (u"ࠫࡸࡪ࡫࠻ࡶࡨࡷࡹ࡮ࡵࡣࠩ᫐") #shift
  bstack11l1l11llll_opy_ = bstack1lll11l_opy_ (u"ࠬࡹࡤ࡬࠼ࡳࡩࡷࡩࡹ࠻ࡦࡲࡻࡳࡲ࡯ࡢࡦࠪ᫑") #shift
  bstack1l1ll1111l_opy_ = bstack1lll11l_opy_ (u"࠭ࡳࡥ࡭࠽ࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫࠺ࡩࡷࡥ࠱ࡲࡧ࡮ࡢࡩࡨࡱࡪࡴࡴࠨ᫒")
  bstack1l1111ll111_opy_ = bstack1lll11l_opy_ (u"ࠧࡴࡦ࡮࠾ࡦ࠷࠱ࡺ࠼ࡶࡥࡻ࡫࠭ࡳࡧࡶࡹࡱࡺࡳࠨ᫓")
  bstack1l11111ll1_opy_ = bstack1lll11l_opy_ (u"ࠨࡵࡧ࡯࠿ࡧ࠱࠲ࡻ࠽ࡨࡷ࡯ࡶࡦࡴ࠰ࡴࡪࡸࡦࡰࡴࡰࡷࡨࡧ࡮ࠨ᫔")
  bstack1ll1l1lll1_opy_ = bstack1lll11l_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡥ࠻࡮ࡲࡧࡦࡲࠧ᫕") #shift
  bstack1lll11ll1l_opy_ = bstack1lll11l_opy_ (u"ࠪࡷࡩࡱ࠺ࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪࡀࡡࡱࡲ࠰ࡹࡵࡲ࡯ࡢࡦࠪ᫖") #shift
  bstack1l1l11ll1_opy_ = bstack1lll11l_opy_ (u"ࠫࡸࡪ࡫࠻ࡣࡸࡸࡴࡳࡡࡵࡧ࠽ࡧ࡮࠳ࡡࡳࡶ࡬ࡪࡦࡩࡴࡴࠩ᫗")
  bstack111111111_opy_ = bstack1lll11l_opy_ (u"ࠬࡹࡤ࡬࠼ࡤ࠵࠶ࡿ࠺ࡨࡧࡷ࠱ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼ࠱ࡷ࡫ࡳࡶ࡮ࡷࡷ࠲ࡹࡵ࡮࡯ࡤࡶࡾ࠭᫘") #shift
  bstack11l1111l1_opy_ = bstack1lll11l_opy_ (u"࠭ࡳࡥ࡭࠽ࡥ࠶࠷ࡹ࠻ࡩࡨࡸ࠲ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࠲ࡸࡥࡴࡷ࡯ࡸࡸ࠭᫙") #shift
  bstack11l11ll1l1l_opy_ = bstack1lll11l_opy_ (u"ࠧࡴࡦ࡮࠾ࡵ࡫ࡲࡤࡻࠪ᫚") #shift
  bstack11lllll1111_opy_ = bstack1lll11l_opy_ (u"ࠨࡵࡧ࡯࠿ࡶࡥࡳࡥࡼ࠾ࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠨ᫛")
  bstack1l111llll_opy_ = bstack1lll11l_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡥ࠻ࡵࡨࡷࡸ࡯࡯࡯࠯ࡶࡸࡦࡺࡵࡴࠩ᫜") #shift
  bstack111lllll1_opy_ = bstack1lll11l_opy_ (u"ࠪࡷࡩࡱ࠺ࡢࡷࡷࡳࡲࡧࡴࡦ࠼࡫ࡹࡧ࠳࡭ࡢࡰࡤ࡫ࡪࡳࡥ࡯ࡶࠪ᫝")
  bstack11l11l1llll_opy_ = bstack1lll11l_opy_ (u"ࠫࡸࡪ࡫࠻ࡲࡵࡳࡽࡿ࠭ࡴࡧࡷࡹࡵ࠭᫞") #shift
  bstack11l1llll11_opy_ = bstack1lll11l_opy_ (u"ࠬࡹࡤ࡬࠼ࡶࡩࡹࡻࡰࠨ᫟")
  bstack11l11ll111l_opy_ = bstack1lll11l_opy_ (u"࠭ࡳࡥ࡭࠽ࡴࡪࡸࡣࡺ࠼ࡶࡲࡦࡶࡳࡩࡱࡷࠫ᫠") # not bstack11l11ll11l1_opy_ in python
  bstack11ll111ll_opy_ = bstack1lll11l_opy_ (u"ࠧࡴࡦ࡮࠾ࡩࡸࡩࡷࡧࡵ࠾ࡶࡻࡩࡵࠩ᫡") # used in bstack11l11llllll_opy_
  bstack1l1l1ll1l_opy_ = bstack1lll11l_opy_ (u"ࠨࡵࡧ࡯࠿ࡪࡲࡪࡸࡨࡶ࠿࡭ࡥࡵࠩ᫢") # used in bstack11l11llllll_opy_
  bstack1ll1l1l111_opy_ = bstack1lll11l_opy_ (u"ࠩࡶࡨࡰࡀࡨࡰࡱ࡮ࠫ᫣")
  bstack11lllll111_opy_ = bstack1lll11l_opy_ (u"ࠪࡷࡩࡱ࠺ࡢࡷࡷࡳࡲࡧࡴࡦ࠼ࡶࡩࡸࡹࡩࡰࡰ࠰ࡲࡦࡳࡥࠨ᫤")
  bstack1l1l11ll11_opy_ = bstack1lll11l_opy_ (u"ࠫࡸࡪ࡫࠻ࡣࡸࡸࡴࡳࡡࡵࡧ࠽ࡷࡪࡹࡳࡪࡱࡱ࠱ࡦࡴ࡮ࡰࡶࡤࡸ࡮ࡵ࡮ࠨ᫥") #
  bstack111llll111_opy_ = bstack1lll11l_opy_ (u"ࠬࡹࡤ࡬࠼ࡲ࠵࠶ࡿ࠺ࡥࡴ࡬ࡺࡪࡸ࠭ࡵࡣ࡮ࡩࡘࡩࡲࡦࡧࡱࡗ࡭ࡵࡴࠨ᫦")
  bstack1l1l11l11l_opy_ = bstack1lll11l_opy_ (u"࠭ࡳࡥ࡭࠽ࡴࡪࡸࡣࡺ࠼ࡤࡹࡹࡵ࠭ࡤࡣࡳࡸࡺࡸࡥࠨ᫧")
  bstack1l1l1ll11l_opy_ = bstack1lll11l_opy_ (u"ࠧࡴࡦ࡮࠾ࡵࡸࡥ࠮ࡶࡨࡷࡹ࠭᫨")
  bstack1ll11l1l1l_opy_ = bstack1lll11l_opy_ (u"ࠨࡵࡧ࡯࠿ࡶ࡯ࡴࡶ࠰ࡸࡪࡹࡴࠨ᫩")
  bstack111ll111l1_opy_ = bstack1lll11l_opy_ (u"ࠩࡶࡨࡰࡀࡤࡳ࡫ࡹࡩࡷࡀࡰࡳࡧ࠰࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡿࡧࡴࡪࡱࡱࠫ᫪") #shift
  bstack1ll11lllll_opy_ = bstack1lll11l_opy_ (u"ࠪࡷࡩࡱ࠺ࡥࡴ࡬ࡺࡪࡸ࠺ࡱࡱࡶࡸ࠲࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡺࡢࡶ࡬ࡳࡳ࠭᫫") #shift
  bstack11l11l1ll11_opy_ = bstack1lll11l_opy_ (u"ࠫࡸࡪ࡫࠻ࡣࡸࡸࡴ࠳ࡣࡢࡲࡷࡹࡷ࡫ࠧ᫬")
  bstack11l11l11ll1_opy_ = bstack1lll11l_opy_ (u"ࠬࡹࡤ࡬࠼ࡤࡹࡹࡵ࡭ࡢࡶࡨ࠾࡮ࡪ࡬ࡦ࠯ࡷ࡭ࡲ࡫࡯ࡶࡶࠪ᫭")
  bstack1l1l11lllll_opy_ = bstack1lll11l_opy_ (u"࠭ࡳࡥ࡭࠽ࡧࡱ࡯࠺ࡴࡶࡤࡶࡹ࠭᫮")
  bstack11l11l1l111_opy_ = bstack1lll11l_opy_ (u"ࠧࡴࡦ࡮࠾ࡨࡲࡩ࠻ࡦࡲࡻࡳࡲ࡯ࡢࡦࠪ᫯")
  bstack11l11ll1lll_opy_ = bstack1lll11l_opy_ (u"ࠨࡵࡧ࡯࠿ࡩ࡬ࡪ࠼ࡦ࡬ࡪࡩ࡫࠮ࡷࡳࡨࡦࡺࡥࠨ᫰")
  bstack1l11ll11l11_opy_ = bstack1lll11l_opy_ (u"ࠩࡶࡨࡰࡀࡣ࡭࡫࠽ࡳࡳ࠳ࡢࡰࡱࡷࡷࡹࡸࡡࡱࠩ᫱")
  bstack1l1l111llll_opy_ = bstack1lll11l_opy_ (u"ࠪࡷࡩࡱ࠺ࡤ࡮࡬࠾ࡴࡴ࠭ࡤࡱࡱࡲࡪࡩࡴࠨ᫲")
  bstack1l1l111l11l_opy_ = bstack1lll11l_opy_ (u"ࠫࡸࡪ࡫࠻ࡥ࡯࡭࠿ࡵ࡮࠮ࡵࡷࡳࡵ࠭᫳")
  bstack1l11ll1l111_opy_ = bstack1lll11l_opy_ (u"ࠬࡹࡤ࡬࠼ࡶࡸࡦࡸࡴࡃ࡫ࡱࡗࡪࡹࡳࡪࡱࡱࠫ᫴")
  bstack1l1l1ll1111_opy_ = bstack1lll11l_opy_ (u"࠭ࡳࡥ࡭࠽ࡧࡴࡴ࡮ࡦࡥࡷࡆ࡮ࡴࡓࡦࡵࡶ࡭ࡴࡴࠧ᫵")
  bstack11l11l1lll1_opy_ = bstack1lll11l_opy_ (u"ࠧࡴࡦ࡮࠾ࡩࡸࡩࡷࡧࡵࡍࡳ࡯ࡴࠨ᫶")
  bstack11l1l11l11l_opy_ = bstack1lll11l_opy_ (u"ࠨࡵࡧ࡯࠿࡬ࡩ࡯ࡦࡑࡩࡦࡸࡥࡴࡶࡋࡹࡧ࠭᫷")
  bstack1llll11lll1_opy_ = bstack1lll11l_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࡎࡴࡩࡵࠩ᫸")
  bstack1lllll1l11l_opy_ = bstack1lll11l_opy_ (u"ࠪࡷࡩࡱ࠺ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡙ࡴࡢࡴࡷࠫ᫹")
  bstack1l111l11111_opy_ = bstack1lll11l_opy_ (u"ࠫࡸࡪ࡫࠻ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡄࡱࡱࡪ࡮࡭ࠧ᫺")
  bstack11l11lll1l1_opy_ = bstack1lll11l_opy_ (u"ࠬࡹࡤ࡬࠼ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࡅࡲࡲ࡫࡯ࡧࠨ᫻")
  bstack1l1ll111lll_opy_ = bstack1lll11l_opy_ (u"࠭ࡳࡥ࡭࠽ࡥ࡮࡙ࡥ࡭ࡨࡋࡩࡦࡲࡓࡵࡧࡳࠫ᫼")
  bstack1l1ll111l11_opy_ = bstack1lll11l_opy_ (u"ࠧࡴࡦ࡮࠾ࡦ࡯ࡓࡦ࡮ࡩࡌࡪࡧ࡬ࡈࡧࡷࡖࡪࡹࡵ࡭ࡶࠪ᫽")
  bstack1l11l11l1ll_opy_ = bstack1lll11l_opy_ (u"ࠨࡵࡧ࡯࠿ࡺࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࡊࡼࡥ࡯ࡶࠪ᫾")
  bstack1l11ll11111_opy_ = bstack1lll11l_opy_ (u"ࠩࡶࡨࡰࡀࡴࡦࡵࡷࡗࡪࡹࡳࡪࡱࡱࡉࡻ࡫࡮ࡵࠩ᫿")
  bstack1l11l1l111l_opy_ = bstack1lll11l_opy_ (u"ࠪࡷࡩࡱ࠺ࡤ࡮࡬࠾ࡱࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࡆࡸࡨࡲࡹ࠭ᬀ")
  bstack11l11l1l1ll_opy_ = bstack1lll11l_opy_ (u"ࠫࡸࡪ࡫࠻ࡥ࡯࡭࠿࡫࡮ࡲࡷࡨࡹࡪ࡚ࡥࡴࡶࡈࡺࡪࡴࡴࠨᬁ")
  bstack1lllll11l11_opy_ = bstack1lll11l_opy_ (u"ࠬࡹࡤ࡬࠼ࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡔࡶࡲࡴࠬᬂ")
  bstack1l1l11l1l1l_opy_ = bstack1lll11l_opy_ (u"࠭ࡳࡥ࡭࠽ࡳࡳ࡙ࡴࡰࡲࠪᬃ")
class STAGE(Enum):
  bstack1ll1lllll_opy_ = bstack1lll11l_opy_ (u"ࠧࡴࡶࡤࡶࡹ࠭ᬄ")
  END = bstack1lll11l_opy_ (u"ࠨࡧࡱࡨࠬᬅ")
  bstack1ll1l1l11_opy_ = bstack1lll11l_opy_ (u"ࠩࡶ࡭ࡳ࡭࡬ࡦࠩᬆ")
bstack1111ll1111_opy_ = {
  bstack1lll11l_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖࠪᬇ"): bstack1lll11l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᬈ"),
  bstack1lll11l_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘ࠲ࡈࡄࡅࠩᬉ"): bstack1lll11l_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠳ࡣࡶࡥࡸࡱࡧ࡫ࡲࠨᬊ")
}
PLAYWRIGHT_HUB_URL = bstack1lll11l_opy_ (u"ࠢࡸࡵࡶ࠾࠴࠵ࡣࡥࡲ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡂࡧࡦࡶࡳ࠾ࠤᬋ")
bstack1l111l11l1l_opy_ = 98
bstack1l11111ll1l_opy_ = 100
bstack1lll11ll1_opy_ = {
  bstack1lll11l_opy_ (u"ࠨࡴࡨࡶࡺࡴࠧᬌ"): bstack1lll11l_opy_ (u"ࠩ࠰࠱ࡷ࡫ࡲࡶࡰࡶࠫᬍ"),
  bstack1lll11l_opy_ (u"ࠪࡨࡪࡲࡡࡺࠩᬎ"): bstack1lll11l_opy_ (u"ࠫ࠲࠳ࡲࡦࡴࡸࡲࡸ࠳ࡤࡦ࡮ࡤࡽࠬᬏ"),
  bstack1lll11l_opy_ (u"ࠬࡸࡥࡳࡷࡱ࠱ࡩ࡫࡬ࡢࡻࠪᬐ"): 0
}
bstack11ll1l1lll1_opy_ = bstack1lll11l_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࡤࡱ࡯ࡰࡪࡩࡴࡰࡴ࠰ࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲࠨᬑ")
bstack11l1l111ll1_opy_ = bstack1lll11l_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࡷࡳࡰࡴࡧࡤ࠮ࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠦᬒ")
bstack1l1llll11l_opy_ = bstack1lll11l_opy_ (u"ࠣࡖࡈࡗ࡙ࠦࡒࡆࡒࡒࡖ࡙ࡏࡎࡈࠢࡄࡒࡉࠦࡁࡏࡃࡏ࡝࡙ࡏࡃࡔࠤᬓ")