# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import re
from enum import Enum
bstack1l111l11ll_opy_ = {
  bstack11l111_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫៅ"): bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡸࡷࡪࡸࠧំ"),
  bstack11l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧះ"): bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡰ࡫ࡹࠨៈ"),
  bstack11l111_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩ៉"): bstack11l111_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠫ៊"),
  bstack11l111_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨ់"): bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡶࡩࡤࡽ࠳ࡤࠩ៌"),
  bstack11l111_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨ៍"): bstack11l111_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࠬ៎"),
  bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ៏"): bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࠬ័"),
  bstack11l111_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ៑"): bstack11l111_opy_ (u"ࠨࡰࡤࡱࡪ្࠭"),
  bstack11l111_opy_ (u"ࠩࡧࡩࡧࡻࡧࠨ៓"): bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡧࡩࡧࡻࡧࠨ។"),
  bstack11l111_opy_ (u"ࠫࡨࡵ࡮ࡴࡱ࡯ࡩࡑࡵࡧࡴࠩ៕"): bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡮ࡴࡱ࡯ࡩࠬ៖"),
  bstack11l111_opy_ (u"࠭࡮ࡦࡶࡺࡳࡷࡱࡌࡰࡩࡶࠫៗ"): bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡮ࡦࡶࡺࡳࡷࡱࡌࡰࡩࡶࠫ៘"),
  bstack11l111_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡍࡱࡪࡷࠬ៙"): bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡳࡴ࡮ࡻ࡭ࡍࡱࡪࡷࠬ៚"),
  bstack11l111_opy_ (u"ࠪࡺ࡮ࡪࡥࡰࠩ៛"): bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡺ࡮ࡪࡥࡰࠩៜ"),
  bstack11l111_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡌࡰࡩࡶࠫ៝"): bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡌࡰࡩࡶࠫ៞"),
  bstack11l111_opy_ (u"ࠧࡵࡧ࡯ࡩࡲ࡫ࡴࡳࡻࡏࡳ࡬ࡹࠧ៟"): bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵࡧ࡯ࡩࡲ࡫ࡴࡳࡻࡏࡳ࡬ࡹࠧ០"),
  bstack11l111_opy_ (u"ࠩࡪࡩࡴࡒ࡯ࡤࡣࡷ࡭ࡴࡴࠧ១"): bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡪࡩࡴࡒ࡯ࡤࡣࡷ࡭ࡴࡴࠧ២"),
  bstack11l111_opy_ (u"ࠫࡹ࡯࡭ࡦࡼࡲࡲࡪ࠭៣"): bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡹ࡯࡭ࡦࡼࡲࡲࡪ࠭៤"),
  bstack11l111_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ៥"): bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ៦"),
  bstack11l111_opy_ (u"ࠨ࡯ࡤࡷࡰࡉ࡯࡮࡯ࡤࡲࡩࡹࠧ៧"): bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡯ࡤࡷࡰࡉ࡯࡮࡯ࡤࡲࡩࡹࠧ៨"),
  bstack11l111_opy_ (u"ࠪ࡭ࡩࡲࡥࡕ࡫ࡰࡩࡴࡻࡴࠨ៩"): bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱࡭ࡩࡲࡥࡕ࡫ࡰࡩࡴࡻࡴࠨ៪"),
  bstack11l111_opy_ (u"ࠬࡳࡡࡴ࡭ࡅࡥࡸ࡯ࡣࡂࡷࡷ࡬ࠬ៫"): bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡳࡡࡴ࡭ࡅࡥࡸ࡯ࡣࡂࡷࡷ࡬ࠬ៬"),
  bstack11l111_opy_ (u"ࠧࡴࡧࡱࡨࡐ࡫ࡹࡴࠩ៭"): bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡴࡧࡱࡨࡐ࡫ࡹࡴࠩ៮"),
  bstack11l111_opy_ (u"ࠩࡤࡹࡹࡵࡗࡢ࡫ࡷࠫ៯"): bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡹࡹࡵࡗࡢ࡫ࡷࠫ៰"),
  bstack11l111_opy_ (u"ࠫ࡭ࡵࡳࡵࡵࠪ៱"): bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡭ࡵࡳࡵࡵࠪ៲"),
  bstack11l111_opy_ (u"࠭ࡢࡧࡥࡤࡧ࡭࡫ࠧ៳"): bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡧࡥࡤࡧ࡭࡫ࠧ៴"),
  bstack11l111_opy_ (u"ࠨࡹࡶࡐࡴࡩࡡ࡭ࡕࡸࡴࡵࡵࡲࡵࠩ៵"): bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡹࡶࡐࡴࡩࡡ࡭ࡕࡸࡴࡵࡵࡲࡵࠩ៶"),
  bstack11l111_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡇࡴࡸࡳࡓࡧࡶࡸࡷ࡯ࡣࡵ࡫ࡲࡲࡸ࠭៷"): bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡨ࡮ࡹࡡࡣ࡮ࡨࡇࡴࡸࡳࡓࡧࡶࡸࡷ࡯ࡣࡵ࡫ࡲࡲࡸ࠭៸"),
  bstack11l111_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩ៹"): bstack11l111_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭៺"),
  bstack11l111_opy_ (u"ࠧࡳࡧࡤࡰࡒࡵࡢࡪ࡮ࡨࠫ៻"): bstack11l111_opy_ (u"ࠨࡴࡨࡥࡱࡥ࡭ࡰࡤ࡬ࡰࡪ࠭៼"),
  bstack11l111_opy_ (u"ࠩࡤࡴࡵ࡯ࡵ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩ៽"): bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡴࡵ࡯ࡵ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠪ៾"),
  bstack11l111_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡒࡪࡺࡷࡰࡴ࡮ࠫ៿"): bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡻࡳࡵࡱࡰࡒࡪࡺࡷࡰࡴ࡮ࠫ᠀"),
  bstack11l111_opy_ (u"࠭࡮ࡦࡶࡺࡳࡷࡱࡐࡳࡱࡩ࡭ࡱ࡫ࠧ᠁"): bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡮ࡦࡶࡺࡳࡷࡱࡐࡳࡱࡩ࡭ࡱ࡫ࠧ᠂"),
  bstack11l111_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡊࡰࡶࡩࡨࡻࡲࡦࡅࡨࡶࡹࡹࠧ᠃"): bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡰࡵࡕࡶࡰࡈ࡫ࡲࡵࡵࠪ᠄"),
  bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬ᠅"): bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬ᠆"),
  bstack11l111_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ᠇"): bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡹ࡯ࡶࡴࡦࡩࠬ᠈"),
  bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ᠉"): bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ᠊"),
  bstack11l111_opy_ (u"ࠩ࡫ࡳࡸࡺࡎࡢ࡯ࡨࠫ᠋"): bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡫ࡳࡸࡺࡎࡢ࡯ࡨࠫ᠌"),
  bstack11l111_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡗ࡮ࡳࠧ᠍"): bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡪࡴࡡࡣ࡮ࡨࡗ࡮ࡳࠧ᠎"),
  bstack11l111_opy_ (u"࠭ࡳࡪ࡯ࡒࡴࡹ࡯࡯࡯ࡵࠪ᠏"): bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡳࡪ࡯ࡒࡴࡹ࡯࡯࡯ࡵࠪ᠐"),
  bstack11l111_opy_ (u"ࠨࡷࡳࡰࡴࡧࡤࡎࡧࡧ࡭ࡦ࠭᠑"): bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡳࡰࡴࡧࡤࡎࡧࡧ࡭ࡦ࠭᠒"),
  bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭᠓"): bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭᠔"),
  bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧ᠕"): bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧ᠖")
}
bstack11l11lll1ll_opy_ = [
  bstack11l111_opy_ (u"ࠧࡰࡵࠪ᠗"),
  bstack11l111_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫ᠘"),
  bstack11l111_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫ᠙"),
  bstack11l111_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ᠚"),
  bstack11l111_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨ᠛"),
  bstack11l111_opy_ (u"ࠬࡸࡥࡢ࡮ࡐࡳࡧ࡯࡬ࡦࠩ᠜"),
  bstack11l111_opy_ (u"࠭ࡡࡱࡲ࡬ࡹࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭᠝"),
]
bstack11111lll1l_opy_ = {
  bstack11l111_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ᠞"): [bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩ᠟"), bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡗࡖࡉࡗࡥࡎࡂࡏࡈࠫᠠ")],
  bstack11l111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᠡ"): bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅࡈࡉࡅࡔࡕࡢࡏࡊ࡟ࠧᠢ"),
  bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨᠣ"): bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡕࡊࡎࡇࡣࡓࡇࡍࡆࠩᠤ"),
  bstack11l111_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᠥ"): bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡔࡒࡎࡊࡉࡔࡠࡐࡄࡑࡊ࠭ᠦ"),
  bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᠧ"): bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬᠨ"),
  bstack11l111_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫᠩ"): bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡇࡒࡂࡎࡏࡉࡑ࡙࡟ࡑࡇࡕࡣࡕࡒࡁࡕࡈࡒࡖࡒ࠭ᠪ"),
  bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪᠫ"): bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࠬᠬ"),
  bstack11l111_opy_ (u"ࠨࡴࡨࡶࡺࡴࡔࡦࡵࡷࡷࠬᠭ"): bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔ࡟ࡕࡇࡖࡘࡘ࠭ᠮ"),
  bstack11l111_opy_ (u"ࠪࡥࡵࡶࠧᠯ"): [bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅࡕࡖ࡟ࡊࡆࠪᠰ"), bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆࡖࡐࠨᠱ")],
  bstack11l111_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨᠲ"): bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡓࡅࡍࡢࡐࡔࡍࡌࡆࡘࡈࡐࠬᠳ"),
  bstack11l111_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᠴ"): bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬᠵ"),
  bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧᠶ"): [bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡑࡅࡗࡊࡘࡖࡂࡄࡌࡐࡎ࡚࡙ࠨᠷ"), bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡕࡉࡕࡕࡒࡕࡋࡑࡋࠬᠸ")],
  bstack11l111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪᠹ"): bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡖࡔࡅࡓࡘࡉࡁࡍࡇࠪᠺ"),
  bstack11l111_opy_ (u"ࠨࡵࡰࡥࡷࡺࡓࡦ࡮ࡨࡧࡹ࡯࡯࡯ࡈࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࡦࡵࡈࡒ࡛࠭ᠻ"): bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡑࡕࡇࡍࡋࡓࡕࡔࡄࡘࡎࡕࡎࡠࡕࡐࡅࡗ࡚࡟ࡔࡇࡏࡉࡈ࡚ࡉࡐࡐࡢࡊࡊࡇࡔࡖࡔࡈࡣࡇࡘࡁࡏࡅࡋࡉࡘ࠭ᠼ")
}
bstack1l11l1l1ll_opy_ = {
  bstack11l111_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬᠽ"): [bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫ࡲࡠࡰࡤࡱࡪ࠭ᠾ"), bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡳࡐࡤࡱࡪ࠭ᠿ")],
  bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩᡀ"): [bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸࡥ࡫ࡦࡻࠪᡁ"), bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪᡂ")],
  bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬᡃ"): bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬᡄ"),
  bstack11l111_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᡅ"): bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᡆ"),
  bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᡇ"): bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᡈ"),
  bstack11l111_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᡉ"): [bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡲࡳࡴࠬᡊ"), bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩᡋ")],
  bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨᡌ"): bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࠪᡍ"),
  bstack11l111_opy_ (u"࠭ࡲࡦࡴࡸࡲ࡙࡫ࡳࡵࡵࠪᡎ"): bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡲࡦࡴࡸࡲ࡙࡫ࡳࡵࡵࠪᡏ"),
  bstack11l111_opy_ (u"ࠨࡣࡳࡴࠬᡐ"): bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡳࡴࠬᡑ"),
  bstack11l111_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬᡒ"): bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴ࡭ࡌࡦࡸࡨࡰࠬᡓ"),
  bstack11l111_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᡔ"): bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᡕ"),
  bstack11l111_opy_ (u"ࠢࡴ࡯ࡤࡶࡹ࡙ࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࡇࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࡥࡴࡅࡏࡍࠧᡖ"): bstack11l111_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠲ࡸࡳࡡࡳࡶࡖࡩࡱ࡫ࡣࡵ࡫ࡲࡲࡋ࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࡩࡸࠨᡗ"),
}
bstack1l1l1lllll_opy_ = {
  bstack11l111_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬᡘ"): bstack11l111_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᡙ"),
  bstack11l111_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᡚ"): [bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᡛ"), bstack11l111_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᡜ")],
  bstack11l111_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᡝ"): bstack11l111_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᡞ"),
  bstack11l111_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭ᡟ"): bstack11l111_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪᡠ"),
  bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩᡡ"): [bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭ᡢ"), bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟࡯ࡣࡰࡩࠬᡣ")],
  bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᡤ"): bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪᡥ"),
  bstack11l111_opy_ (u"ࠩࡵࡩࡦࡲࡍࡰࡤ࡬ࡰࡪ࠭ᡦ"): bstack11l111_opy_ (u"ࠪࡶࡪࡧ࡬ࡠ࡯ࡲࡦ࡮ࡲࡥࠨᡧ"),
  bstack11l111_opy_ (u"ࠫࡦࡶࡰࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫᡨ"): [bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡶࡰࡪࡷࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᡩ"), bstack11l111_opy_ (u"࠭ࡡࡱࡲ࡬ࡹࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᡪ")],
  bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡉ࡯ࡵࡨࡧࡺࡸࡥࡄࡧࡵࡸࡸ࠭ᡫ"): [bstack11l111_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡔࡵ࡯ࡇࡪࡸࡴࡴࠩᡬ"), bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡰࡵࡕࡶࡰࡈ࡫ࡲࡵࠩᡭ")]
}
bstack1l1l11111l_opy_ = [
  bstack11l111_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡌࡲࡸ࡫ࡣࡶࡴࡨࡇࡪࡸࡴࡴࠩᡮ"),
  bstack11l111_opy_ (u"ࠫࡵࡧࡧࡦࡎࡲࡥࡩ࡙ࡴࡳࡣࡷࡩ࡬ࡿࠧᡯ"),
  bstack11l111_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫᡰ"),
  bstack11l111_opy_ (u"࠭ࡳࡦࡶ࡚࡭ࡳࡪ࡯ࡸࡔࡨࡧࡹ࠭ᡱ"),
  bstack11l111_opy_ (u"ࠧࡵ࡫ࡰࡩࡴࡻࡴࡴࠩᡲ"),
  bstack11l111_opy_ (u"ࠨࡵࡷࡶ࡮ࡩࡴࡇ࡫࡯ࡩࡎࡴࡴࡦࡴࡤࡧࡹࡧࡢࡪ࡮࡬ࡸࡾ࠭ᡳ"),
  bstack11l111_opy_ (u"ࠩࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡕࡸ࡯࡮ࡲࡷࡆࡪ࡮ࡡࡷ࡫ࡲࡶࠬᡴ"),
  bstack11l111_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᡵ"),
  bstack11l111_opy_ (u"ࠫࡲࡵࡺ࠻ࡨ࡬ࡶࡪ࡬࡯ࡹࡑࡳࡸ࡮ࡵ࡮ࡴࠩᡶ"),
  bstack11l111_opy_ (u"ࠬࡳࡳ࠻ࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᡷ"),
  bstack11l111_opy_ (u"࠭ࡳࡦ࠼࡬ࡩࡔࡶࡴࡪࡱࡱࡷࠬᡸ"),
  bstack11l111_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨ᡹"),
]
bstack11lll11111_opy_ = [
  bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ᡺"),
  bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭᡻"),
  bstack11l111_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᡼"),
  bstack11l111_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ᡽"),
  bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ᡾"),
  bstack11l111_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨ᡿"),
  bstack11l111_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪᢀ"),
  bstack11l111_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬᢁ"),
  bstack11l111_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬᢂ"),
  bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠨᢃ"),
  bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨᢄ"),
  bstack11l111_opy_ (u"ࠬࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࠬᢅ"),
  bstack11l111_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠨᢆ"),
  bstack11l111_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡔࡢࡩࠪᢇ"),
  bstack11l111_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᢈ"),
  bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᢉ"),
  bstack11l111_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡖࡨࡷࡹࡹࠧᢊ"),
  bstack11l111_opy_ (u"ࠫࡈ࡛ࡓࡕࡑࡐࡣ࡙ࡇࡇࡠ࠳ࠪᢋ"),
  bstack11l111_opy_ (u"ࠬࡉࡕࡔࡖࡒࡑࡤ࡚ࡁࡈࡡ࠵ࠫᢌ"),
  bstack11l111_opy_ (u"࠭ࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢ࠷ࠬᢍ"),
  bstack11l111_opy_ (u"ࠧࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣ࠹࠭ᢎ"),
  bstack11l111_opy_ (u"ࠨࡅࡘࡗ࡙ࡕࡍࡠࡖࡄࡋࡤ࠻ࠧᢏ"),
  bstack11l111_opy_ (u"ࠩࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࠶ࠨᢐ"),
  bstack11l111_opy_ (u"ࠪࡇ࡚࡙ࡔࡐࡏࡢࡘࡆࡍ࡟࠸ࠩᢑ"),
  bstack11l111_opy_ (u"ࠫࡈ࡛ࡓࡕࡑࡐࡣ࡙ࡇࡇࡠ࠺ࠪᢒ"),
  bstack11l111_opy_ (u"ࠬࡉࡕࡔࡖࡒࡑࡤ࡚ࡁࡈࡡ࠼ࠫᢓ"),
  bstack11l111_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬᢔ"),
  bstack11l111_opy_ (u"ࠧࡱࡧࡵࡧࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᢕ"),
  bstack11l111_opy_ (u"ࠨࡲࡨࡶࡨࡿࡃࡢࡲࡷࡹࡷ࡫ࡍࡰࡦࡨࠫᢖ"),
  bstack11l111_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫᢗ"),
  bstack11l111_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧᢘ"),
  bstack11l111_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᢙ"),
  bstack11l111_opy_ (u"ࠬࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡑࡳࡸ࡮ࡵ࡮ࡴࠩᢚ")
]
bstack11l11ll1l11_opy_ = [
  bstack11l111_opy_ (u"࠭ࡵࡱ࡮ࡲࡥࡩࡓࡥࡥ࡫ࡤࠫᢛ"),
  bstack11l111_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩᢜ"),
  bstack11l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫᢝ"),
  bstack11l111_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧᢞ"),
  bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡑࡴ࡬ࡳࡷ࡯ࡴࡺࠩᢟ"),
  bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧᢠ"),
  bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡘࡦ࡭ࠧᢡ"),
  bstack11l111_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᢢ"),
  bstack11l111_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩᢣ"),
  bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ᢤ"),
  bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᢥ"),
  bstack11l111_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࠩᢦ"),
  bstack11l111_opy_ (u"ࠫࡴࡹࠧᢧ"),
  bstack11l111_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨᢨ"),
  bstack11l111_opy_ (u"࠭ࡨࡰࡵࡷࡷᢩࠬ"),
  bstack11l111_opy_ (u"ࠧࡢࡷࡷࡳ࡜ࡧࡩࡵࠩᢪ"),
  bstack11l111_opy_ (u"ࠨࡴࡨ࡫࡮ࡵ࡮ࠨ᢫"),
  bstack11l111_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡺࡰࡰࡨࠫ᢬"),
  bstack11l111_opy_ (u"ࠪࡱࡦࡩࡨࡪࡰࡨࠫ᢭"),
  bstack11l111_opy_ (u"ࠫࡷ࡫ࡳࡰ࡮ࡸࡸ࡮ࡵ࡮ࠨ᢮"),
  bstack11l111_opy_ (u"ࠬ࡯ࡤ࡭ࡧࡗ࡭ࡲ࡫࡯ࡶࡶࠪ᢯"),
  bstack11l111_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡕࡲࡪࡧࡱࡸࡦࡺࡩࡰࡰࠪᢰ"),
  bstack11l111_opy_ (u"ࠧࡷ࡫ࡧࡩࡴ࠭ᢱ"),
  bstack11l111_opy_ (u"ࠨࡰࡲࡔࡦ࡭ࡥࡍࡱࡤࡨ࡙࡯࡭ࡦࡱࡸࡸࠬᢲ"),
  bstack11l111_opy_ (u"ࠩࡥࡪࡨࡧࡣࡩࡧࠪᢳ"),
  bstack11l111_opy_ (u"ࠪࡨࡪࡨࡵࡨࠩᢴ"),
  bstack11l111_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡗࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨᢵ"),
  bstack11l111_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡘ࡫࡮ࡥࡍࡨࡽࡸ࠭ᢶ"),
  bstack11l111_opy_ (u"࠭ࡲࡦࡣ࡯ࡑࡴࡨࡩ࡭ࡧࠪᢷ"),
  bstack11l111_opy_ (u"ࠧ࡯ࡱࡓ࡭ࡵ࡫࡬ࡪࡰࡨࠫᢸ"),
  bstack11l111_opy_ (u"ࠨࡥ࡫ࡩࡨࡱࡕࡓࡎࠪᢹ"),
  bstack11l111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᢺ"),
  bstack11l111_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡆࡳࡴࡱࡩࡦࡵࠪᢻ"),
  bstack11l111_opy_ (u"ࠫࡨࡧࡰࡵࡷࡵࡩࡈࡸࡡࡴࡪࠪᢼ"),
  bstack11l111_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩᢽ"),
  bstack11l111_opy_ (u"࠭ࡡࡱࡲ࡬ࡹࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᢾ"),
  bstack11l111_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱ࡚ࡪࡸࡳࡪࡱࡱࠫᢿ"),
  bstack11l111_opy_ (u"ࠨࡰࡲࡆࡱࡧ࡮࡬ࡒࡲࡰࡱ࡯࡮ࡨࠩᣀ"),
  bstack11l111_opy_ (u"ࠩࡰࡥࡸࡱࡓࡦࡰࡧࡏࡪࡿࡳࠨᣁ"),
  bstack11l111_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡏࡳ࡬ࡹࠧᣂ"),
  bstack11l111_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡍࡩ࠭ᣃ"),
  bstack11l111_opy_ (u"ࠬࡪࡥࡥ࡫ࡦࡥࡹ࡫ࡤࡅࡧࡹ࡭ࡨ࡫ࠧᣄ"),
  bstack11l111_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡖࡡࡳࡣࡰࡷࠬᣅ"),
  bstack11l111_opy_ (u"ࠧࡱࡪࡲࡲࡪࡔࡵ࡮ࡤࡨࡶࠬᣆ"),
  bstack11l111_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸ࠭ᣇ"),
  bstack11l111_opy_ (u"ࠩࡱࡩࡹࡽ࡯ࡳ࡭ࡏࡳ࡬ࡹࡏࡱࡶ࡬ࡳࡳࡹࠧᣈ"),
  bstack11l111_opy_ (u"ࠪࡧࡴࡴࡳࡰ࡮ࡨࡐࡴ࡭ࡳࠨᣉ"),
  bstack11l111_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫᣊ"),
  bstack11l111_opy_ (u"ࠬࡧࡰࡱ࡫ࡸࡱࡑࡵࡧࡴࠩᣋ"),
  bstack11l111_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡈࡩࡰ࡯ࡨࡸࡷ࡯ࡣࠨᣌ"),
  bstack11l111_opy_ (u"ࠧࡷ࡫ࡧࡩࡴ࡜࠲ࠨᣍ"),
  bstack11l111_opy_ (u"ࠨ࡯࡬ࡨࡘ࡫ࡳࡴ࡫ࡲࡲࡎࡴࡳࡵࡣ࡯ࡰࡆࡶࡰࡴࠩᣎ"),
  bstack11l111_opy_ (u"ࠩࡨࡷࡵࡸࡥࡴࡵࡲࡗࡪࡸࡶࡦࡴࠪᣏ"),
  bstack11l111_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࡑࡵࡧࡴࠩᣐ"),
  bstack11l111_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡉࡤࡱࠩᣑ"),
  bstack11l111_opy_ (u"ࠬࡺࡥ࡭ࡧࡰࡩࡹࡸࡹࡍࡱࡪࡷࠬᣒ"),
  bstack11l111_opy_ (u"࠭ࡳࡺࡰࡦࡘ࡮ࡳࡥࡘ࡫ࡷ࡬ࡓ࡚ࡐࠨᣓ"),
  bstack11l111_opy_ (u"ࠧࡨࡧࡲࡐࡴࡩࡡࡵ࡫ࡲࡲࠬᣔ"),
  bstack11l111_opy_ (u"ࠨࡩࡳࡷࡑࡵࡣࡢࡶ࡬ࡳࡳ࠭ᣕ"),
  bstack11l111_opy_ (u"ࠩࡱࡩࡹࡽ࡯ࡳ࡭ࡓࡶࡴ࡬ࡩ࡭ࡧࠪᣖ"),
  bstack11l111_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡑࡩࡹࡽ࡯ࡳ࡭ࠪᣗ"),
  bstack11l111_opy_ (u"ࠫ࡫ࡵࡲࡤࡧࡆ࡬ࡦࡴࡧࡦࡌࡤࡶࠬᣘ"),
  bstack11l111_opy_ (u"ࠬࡾ࡭ࡴࡌࡤࡶࠬᣙ"),
  bstack11l111_opy_ (u"࠭ࡸ࡮ࡺࡍࡥࡷ࠭ᣚ"),
  bstack11l111_opy_ (u"ࠧ࡮ࡣࡶ࡯ࡈࡵ࡭࡮ࡣࡱࡨࡸ࠭ᣛ"),
  bstack11l111_opy_ (u"ࠨ࡯ࡤࡷࡰࡈࡡࡴ࡫ࡦࡅࡺࡺࡨࠨᣜ"),
  bstack11l111_opy_ (u"ࠩࡺࡷࡑࡵࡣࡢ࡮ࡖࡹࡵࡶ࡯ࡳࡶࠪᣝ"),
  bstack11l111_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡇࡴࡸࡳࡓࡧࡶࡸࡷ࡯ࡣࡵ࡫ࡲࡲࡸ࠭ᣞ"),
  bstack11l111_opy_ (u"ࠫࡦࡶࡰࡗࡧࡵࡷ࡮ࡵ࡮ࠨᣟ"),
  bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡳࡸࡎࡴࡳࡦࡥࡸࡶࡪࡉࡥࡳࡶࡶࠫᣠ"),
  bstack11l111_opy_ (u"࠭ࡲࡦࡵ࡬࡫ࡳࡇࡰࡱࠩᣡ"),
  bstack11l111_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡰ࡬ࡱࡦࡺࡩࡰࡰࡶࠫᣢ"),
  bstack11l111_opy_ (u"ࠨࡥࡤࡲࡦࡸࡹࠨᣣ"),
  bstack11l111_opy_ (u"ࠩࡩ࡭ࡷ࡫ࡦࡰࡺࠪᣤ"),
  bstack11l111_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪᣥ"),
  bstack11l111_opy_ (u"ࠫ࡮࡫ࠧᣦ"),
  bstack11l111_opy_ (u"ࠬ࡫ࡤࡨࡧࠪᣧ"),
  bstack11l111_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠭ᣨ"),
  bstack11l111_opy_ (u"ࠧࡲࡷࡨࡹࡪ࠭ᣩ"),
  bstack11l111_opy_ (u"ࠨ࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪᣪ"),
  bstack11l111_opy_ (u"ࠩࡤࡴࡵ࡙ࡴࡰࡴࡨࡇࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠪᣫ"),
  bstack11l111_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡆࡥࡲ࡫ࡲࡢࡋࡰࡥ࡬࡫ࡉ࡯࡬ࡨࡧࡹ࡯࡯࡯ࠩᣬ"),
  bstack11l111_opy_ (u"ࠫࡳ࡫ࡴࡸࡱࡵ࡯ࡑࡵࡧࡴࡇࡻࡧࡱࡻࡤࡦࡊࡲࡷࡹࡹࠧᣭ"),
  bstack11l111_opy_ (u"ࠬࡴࡥࡵࡹࡲࡶࡰࡒ࡯ࡨࡵࡌࡲࡨࡲࡵࡥࡧࡋࡳࡸࡺࡳࠨᣮ"),
  bstack11l111_opy_ (u"࠭ࡵࡱࡦࡤࡸࡪࡇࡰࡱࡕࡨࡸࡹ࡯࡮ࡨࡵࠪᣯ"),
  bstack11l111_opy_ (u"ࠧࡳࡧࡶࡩࡷࡼࡥࡅࡧࡹ࡭ࡨ࡫ࠧᣰ"),
  bstack11l111_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨᣱ"),
  bstack11l111_opy_ (u"ࠩࡶࡩࡳࡪࡋࡦࡻࡶࠫᣲ"),
  bstack11l111_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡓࡥࡸࡹࡣࡰࡦࡨࠫᣳ"),
  bstack11l111_opy_ (u"ࠫࡺࡶࡤࡢࡶࡨࡍࡴࡹࡄࡦࡸ࡬ࡧࡪ࡙ࡥࡵࡶ࡬ࡲ࡬ࡹࠧᣴ"),
  bstack11l111_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡆࡻࡤࡪࡱࡌࡲ࡯࡫ࡣࡵ࡫ࡲࡲࠬᣵ"),
  bstack11l111_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡇࡰࡱ࡮ࡨࡔࡦࡿࠧ᣶"),
  bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨ᣷"),
  bstack11l111_opy_ (u"ࠨࡹࡧ࡭ࡴ࡙ࡥࡳࡸ࡬ࡧࡪ࠭᣸"),
  bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫ᣹"),
  bstack11l111_opy_ (u"ࠪࡴࡷ࡫ࡶࡦࡰࡷࡇࡷࡵࡳࡴࡕ࡬ࡸࡪ࡚ࡲࡢࡥ࡮࡭ࡳ࡭ࠧ᣺"),
  bstack11l111_opy_ (u"ࠫ࡭࡯ࡧࡩࡅࡲࡲࡹࡸࡡࡴࡶࠪ᣻"),
  bstack11l111_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡕࡸࡥࡧࡧࡵࡩࡳࡩࡥࡴࠩ᣼"),
  bstack11l111_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪ࡙ࡩ࡮ࠩ᣽"),
  bstack11l111_opy_ (u"ࠧࡴ࡫ࡰࡓࡵࡺࡩࡰࡰࡶࠫ᣾"),
  bstack11l111_opy_ (u"ࠨࡴࡨࡱࡴࡼࡥࡊࡑࡖࡅࡵࡶࡓࡦࡶࡷ࡭ࡳ࡭ࡳࡍࡱࡦࡥࡱ࡯ࡺࡢࡶ࡬ࡳࡳ࠭᣿"),
  bstack11l111_opy_ (u"ࠩ࡫ࡳࡸࡺࡎࡢ࡯ࡨࠫᤀ"),
  bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬᤁ"),
  bstack11l111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࠭ᤂ"),
  bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠫᤃ"),
  bstack11l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᤄ"),
  bstack11l111_opy_ (u"ࠧࡱࡣࡪࡩࡑࡵࡡࡥࡕࡷࡶࡦࡺࡥࡨࡻࠪᤅ"),
  bstack11l111_opy_ (u"ࠨࡲࡵࡳࡽࡿࠧᤆ"),
  bstack11l111_opy_ (u"ࠩࡷ࡭ࡲ࡫࡯ࡶࡶࡶࠫᤇ"),
  bstack11l111_opy_ (u"ࠪࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡖࡲࡰ࡯ࡳࡸࡇ࡫ࡨࡢࡸ࡬ࡳࡷ࠭ᤈ")
]
bstack11l1l1ll1_opy_ = {
  bstack11l111_opy_ (u"ࠫࡻ࠭ᤉ"): bstack11l111_opy_ (u"ࠬࡼࠧᤊ"),
  bstack11l111_opy_ (u"࠭ࡦࠨᤋ"): bstack11l111_opy_ (u"ࠧࡧࠩᤌ"),
  bstack11l111_opy_ (u"ࠨࡨࡲࡶࡨ࡫ࠧᤍ"): bstack11l111_opy_ (u"ࠩࡩࡳࡷࡩࡥࠨᤎ"),
  bstack11l111_opy_ (u"ࠪࡳࡳࡲࡹࡢࡷࡷࡳࡲࡧࡴࡦࠩᤏ"): bstack11l111_opy_ (u"ࠫࡴࡴ࡬ࡺࡃࡸࡸࡴࡳࡡࡵࡧࠪᤐ"),
  bstack11l111_opy_ (u"ࠬ࡬࡯ࡳࡥࡨࡰࡴࡩࡡ࡭ࠩᤑ"): bstack11l111_opy_ (u"࠭ࡦࡰࡴࡦࡩࡱࡵࡣࡢ࡮ࠪᤒ"),
  bstack11l111_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡮࡯ࡴࡶࠪᤓ"): bstack11l111_opy_ (u"ࠨࡲࡵࡳࡽࡿࡈࡰࡵࡷࠫᤔ"),
  bstack11l111_opy_ (u"ࠩࡳࡶࡴࡾࡹࡱࡱࡵࡸࠬᤕ"): bstack11l111_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡲࡶࡹ࠭ᤖ"),
  bstack11l111_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡸࡷࡪࡸࠧᤗ"): bstack11l111_opy_ (u"ࠬࡶࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨᤘ"),
  bstack11l111_opy_ (u"࠭ࡰࡳࡱࡻࡽࡵࡧࡳࡴࠩᤙ"): bstack11l111_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖࡡࡴࡵࠪᤚ"),
  bstack11l111_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡰࡳࡱࡻࡽ࡭ࡵࡳࡵࠩᤛ"): bstack11l111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡑࡴࡲࡼࡾࡎ࡯ࡴࡶࠪᤜ"),
  bstack11l111_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡲࡵࡳࡽࡿࡰࡰࡴࡷࠫᤝ"): bstack11l111_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡑࡱࡵࡸࠬᤞ"),
  bstack11l111_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡴࡷࡵࡸࡺࡷࡶࡩࡷ࠭᤟"): bstack11l111_opy_ (u"࠭࠭࡭ࡱࡦࡥࡱࡖࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨᤠ"),
  bstack11l111_opy_ (u"ࠧ࠮࡮ࡲࡧࡦࡲࡰࡳࡱࡻࡽࡺࡹࡥࡳࠩᤡ"): bstack11l111_opy_ (u"ࠨ࠯࡯ࡳࡨࡧ࡬ࡑࡴࡲࡼࡾ࡛ࡳࡦࡴࠪᤢ"),
  bstack11l111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡱࡴࡲࡼࡾࡶࡡࡴࡵࠪᤣ"): bstack11l111_opy_ (u"ࠪ࠱ࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡑࡣࡶࡷࠬᤤ"),
  bstack11l111_opy_ (u"ࠫ࠲ࡲ࡯ࡤࡣ࡯ࡴࡷࡵࡸࡺࡲࡤࡷࡸ࠭ᤥ"): bstack11l111_opy_ (u"ࠬ࠳࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡓࡥࡸࡹࠧᤦ"),
  bstack11l111_opy_ (u"࠭ࡢࡪࡰࡤࡶࡾࡶࡡࡵࡪࠪᤧ"): bstack11l111_opy_ (u"ࠧࡣ࡫ࡱࡥࡷࡿࡰࡢࡶ࡫ࠫᤨ"),
  bstack11l111_opy_ (u"ࠨࡲࡤࡧ࡫࡯࡬ࡦࠩᤩ"): bstack11l111_opy_ (u"ࠩ࠰ࡴࡦࡩ࠭ࡧ࡫࡯ࡩࠬᤪ"),
  bstack11l111_opy_ (u"ࠪࡴࡦࡩ࠭ࡧ࡫࡯ࡩࠬᤫ"): bstack11l111_opy_ (u"ࠫ࠲ࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧ᤬"),
  bstack11l111_opy_ (u"ࠬ࠳ࡰࡢࡥ࠰ࡪ࡮ࡲࡥࠨ᤭"): bstack11l111_opy_ (u"࠭࠭ࡱࡣࡦ࠱࡫࡯࡬ࡦࠩ᤮"),
  bstack11l111_opy_ (u"ࠧ࡭ࡱࡪࡪ࡮ࡲࡥࠨ᤯"): bstack11l111_opy_ (u"ࠨ࡮ࡲ࡫࡫࡯࡬ࡦࠩᤰ"),
  bstack11l111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᤱ"): bstack11l111_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬᤲ"),
  bstack11l111_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰ࠱ࡷ࡫ࡰࡦࡣࡷࡩࡷ࠭ᤳ"): bstack11l111_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡗ࡫ࡰࡦࡣࡷࡩࡷ࠭ᤴ")
}
bstack11l11ll111l_opy_ = bstack11l111_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࡨ࡫ࡷ࡬ࡺࡨ࠮ࡤࡱࡰ࠳ࡵ࡫ࡲࡤࡻ࠲ࡧࡱ࡯࠯ࡳࡧ࡯ࡩࡦࡹࡥࡴ࠱࡯ࡥࡹ࡫ࡳࡵ࠱ࡧࡳࡼࡴ࡬ࡰࡣࡧࠦᤵ")
bstack11l11ll1111_opy_ = bstack11l111_opy_ (u"ࠢ࠰ࡲࡨࡶࡨࡿ࠯ࡩࡧࡤࡰࡹ࡮ࡣࡩࡧࡦ࡯ࠧᤶ")
bstack111l111l11_opy_ = bstack11l111_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࡨࡨࡸ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡶࡩࡳࡪ࡟ࡴࡦ࡮ࡣࡪࡼࡥ࡯ࡶࡶࠦᤷ")
bstack11ll11l11_opy_ = bstack11l111_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲࡬ࡺࡨ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡻࡩ࠵ࡨࡶࡤࠪᤸ")
bstack1ll1l1l1ll_opy_ = bstack11l111_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲࡬ࡺࡨ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧ᤹࠭")
bstack1111111l1_opy_ = bstack11l111_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴࡮ࡵࡣ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡴࡥࡹࡶࡢ࡬ࡺࡨࡳࠨ᤺")
bstack11l11l1ll11_opy_ = {
  bstack11l111_opy_ (u"ࠬࡩࡲࡪࡶ࡬ࡧࡦࡲ᤻ࠧ"): 50,
  bstack11l111_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ᤼"): 40,
  bstack11l111_opy_ (u"ࠧࡸࡣࡵࡲ࡮ࡴࡧࠨ᤽"): 30,
  bstack11l111_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭᤾"): 20,
  bstack11l111_opy_ (u"ࠩࡧࡩࡧࡻࡧࠨ᤿"): 10
}
bstack1111l1lll_opy_ = bstack11l11l1ll11_opy_[bstack11l111_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨ᥀")]
bstack111l1111l1_opy_ = bstack11l111_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠱ࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࠪ᥁")
bstack1l1ll1ll11_opy_ = bstack11l111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱ࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࠪ᥂")
bstack11llll1ll1_opy_ = bstack11l111_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠳ࡰࡺࡶ࡫ࡳࡳࡧࡧࡦࡰࡷ࠳ࠬ᥃")
bstack1l1l11l111_opy_ = bstack11l111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡱࡻࡷ࡬ࡴࡴࡡࡨࡧࡱࡸ࠴࠭᥄")
bstack1lll11l11_opy_ = bstack11l111_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵࠢࡤࡲࡩࠦࡰࡺࡶࡨࡷࡹ࠳ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠡࡲࡤࡧࡰࡧࡧࡦࡵ࠱ࠤࡥࡶࡩࡱࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶࠣࡴࡾࡺࡥࡴࡶ࠰ࡷࡪࡲࡥ࡯࡫ࡸࡱࡥ࠭᥅")
bstack11l1l111lll_opy_ = [bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡗࡖࡉࡗࡔࡁࡎࡇࠪ᥆"), bstack11l111_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡗࡖࡉࡗࡔࡁࡎࡇࠪ᥇")]
bstack11l1l111l11_opy_ = [bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅࡈࡉࡅࡔࡕࡢࡏࡊ࡟ࠧ᥈"), bstack11l111_opy_ (u"ࠬ࡟ࡏࡖࡔࡢࡅࡈࡉࡅࡔࡕࡢࡏࡊ࡟ࠧ᥉")]
bstack11lll11ll_opy_ = re.compile(bstack11l111_opy_ (u"࠭࡞࡜࡞࡟ࡻ࠲ࡣࠫ࠻࠰࠭ࠨࠬ᥊"))
bstack1l111ll1l1_opy_ = [
  bstack11l111_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡒࡦࡳࡥࠨ᥋"),
  bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ᥌"),
  bstack11l111_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭᥍"),
  bstack11l111_opy_ (u"ࠪࡲࡪࡽࡃࡰ࡯ࡰࡥࡳࡪࡔࡪ࡯ࡨࡳࡺࡺࠧ᥎"),
  bstack11l111_opy_ (u"ࠫࡦࡶࡰࠨ᥏"),
  bstack11l111_opy_ (u"ࠬࡻࡤࡪࡦࠪᥐ"),
  bstack11l111_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࠨᥑ"),
  bstack11l111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࡫ࠧᥒ"),
  bstack11l111_opy_ (u"ࠨࡱࡵ࡭ࡪࡴࡴࡢࡶ࡬ࡳࡳ࠭ᥓ"),
  bstack11l111_opy_ (u"ࠩࡤࡹࡹࡵࡗࡦࡤࡹ࡭ࡪࡽࠧᥔ"),
  bstack11l111_opy_ (u"ࠪࡲࡴࡘࡥࡴࡧࡷࠫᥕ"), bstack11l111_opy_ (u"ࠫ࡫ࡻ࡬࡭ࡔࡨࡷࡪࡺࠧᥖ"),
  bstack11l111_opy_ (u"ࠬࡩ࡬ࡦࡣࡵࡗࡾࡹࡴࡦ࡯ࡉ࡭ࡱ࡫ࡳࠨᥗ"),
  bstack11l111_opy_ (u"࠭ࡥࡷࡧࡱࡸ࡙࡯࡭ࡪࡰࡪࡷࠬᥘ"),
  bstack11l111_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡐࡦࡴࡩࡳࡷࡳࡡ࡯ࡥࡨࡐࡴ࡭ࡧࡪࡰࡪࠫᥙ"),
  bstack11l111_opy_ (u"ࠨࡱࡷ࡬ࡪࡸࡁࡱࡲࡶࠫᥚ"),
  bstack11l111_opy_ (u"ࠩࡳࡶ࡮ࡴࡴࡑࡣࡪࡩࡘࡵࡵࡳࡥࡨࡓࡳࡌࡩ࡯ࡦࡉࡥ࡮ࡲࡵࡳࡧࠪᥛ"),
  bstack11l111_opy_ (u"ࠪࡥࡵࡶࡁࡤࡶ࡬ࡺ࡮ࡺࡹࠨᥜ"), bstack11l111_opy_ (u"ࠫࡦࡶࡰࡑࡣࡦ࡯ࡦ࡭ࡥࠨᥝ"), bstack11l111_opy_ (u"ࠬࡧࡰࡱ࡙ࡤ࡭ࡹࡇࡣࡵ࡫ࡹ࡭ࡹࡿࠧᥞ"), bstack11l111_opy_ (u"࠭ࡡࡱࡲ࡚ࡥ࡮ࡺࡐࡢࡥ࡮ࡥ࡬࡫ࠧᥟ"), bstack11l111_opy_ (u"ࠧࡢࡲࡳ࡛ࡦ࡯ࡴࡅࡷࡵࡥࡹ࡯࡯࡯ࠩᥠ"),
  bstack11l111_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡓࡧࡤࡨࡾ࡚ࡩ࡮ࡧࡲࡹࡹ࠭ᥡ"),
  bstack11l111_opy_ (u"ࠩࡤࡰࡱࡵࡷࡕࡧࡶࡸࡕࡧࡣ࡬ࡣࡪࡩࡸ࠭ᥢ"),
  bstack11l111_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࡇࡴࡼࡥࡳࡣࡪࡩࠬᥣ"), bstack11l111_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࡈࡵࡶࡦࡴࡤ࡫ࡪࡋ࡮ࡥࡋࡱࡸࡪࡴࡴࠨᥤ"),
  bstack11l111_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩࡊࡥࡷ࡫ࡦࡩࡗ࡫ࡡࡥࡻࡗ࡭ࡲ࡫࡯ࡶࡶࠪᥥ"),
  bstack11l111_opy_ (u"࠭ࡡࡥࡤࡓࡳࡷࡺࠧᥦ"),
  bstack11l111_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࡅࡧࡹ࡭ࡨ࡫ࡓࡰࡥ࡮ࡩࡹ࠭ᥧ"),
  bstack11l111_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࡋࡱࡷࡹࡧ࡬࡭ࡖ࡬ࡱࡪࡵࡵࡵࠩᥨ"),
  bstack11l111_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡌࡲࡸࡺࡡ࡭࡮ࡓࡥࡹ࡮ࠧᥩ"),
  bstack11l111_opy_ (u"ࠪࡥࡻࡪࠧᥪ"), bstack11l111_opy_ (u"ࠫࡦࡼࡤࡍࡣࡸࡲࡨ࡮ࡔࡪ࡯ࡨࡳࡺࡺࠧᥫ"), bstack11l111_opy_ (u"ࠬࡧࡶࡥࡔࡨࡥࡩࡿࡔࡪ࡯ࡨࡳࡺࡺࠧᥬ"), bstack11l111_opy_ (u"࠭ࡡࡷࡦࡄࡶ࡬ࡹࠧᥭ"),
  bstack11l111_opy_ (u"ࠧࡶࡵࡨࡏࡪࡿࡳࡵࡱࡵࡩࠬ᥮"), bstack11l111_opy_ (u"ࠨ࡭ࡨࡽࡸࡺ࡯ࡳࡧࡓࡥࡹ࡮ࠧ᥯"), bstack11l111_opy_ (u"ࠩ࡮ࡩࡾࡹࡴࡰࡴࡨࡔࡦࡹࡳࡸࡱࡵࡨࠬᥰ"),
  bstack11l111_opy_ (u"ࠪ࡯ࡪࡿࡁ࡭࡫ࡤࡷࠬᥱ"), bstack11l111_opy_ (u"ࠫࡰ࡫ࡹࡑࡣࡶࡷࡼࡵࡲࡥࠩᥲ"),
  bstack11l111_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡩࡸࡩࡷࡧࡵࡉࡽ࡫ࡣࡶࡶࡤࡦࡱ࡫ࠧᥳ"), bstack11l111_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡪࡲࡪࡸࡨࡶࡆࡸࡧࡴࠩᥴ"), bstack11l111_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷࡋࡸࡦࡥࡸࡸࡦࡨ࡬ࡦࡆ࡬ࡶࠬ᥵"), bstack11l111_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡥࡴ࡬ࡺࡪࡸࡃࡩࡴࡲࡱࡪࡓࡡࡱࡲ࡬ࡲ࡬ࡌࡩ࡭ࡧࠪ᥶"), bstack11l111_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡦࡵ࡭ࡻ࡫ࡲࡖࡵࡨࡗࡾࡹࡴࡦ࡯ࡈࡼࡪࡩࡵࡵࡣࡥࡰࡪ࠭᥷"),
  bstack11l111_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡧࡶ࡮ࡼࡥࡳࡒࡲࡶࡹ࠭᥸"), bstack11l111_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡨࡷ࡯ࡶࡦࡴࡓࡳࡷࡺࡳࠨ᥹"),
  bstack11l111_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡩࡸࡩࡷࡧࡵࡈ࡮ࡹࡡࡣ࡮ࡨࡆࡺ࡯࡬ࡥࡅ࡫ࡩࡨࡱࠧ᥺"),
  bstack11l111_opy_ (u"࠭ࡡࡶࡶࡲ࡛ࡪࡨࡶࡪࡧࡺࡘ࡮ࡳࡥࡰࡷࡷࠫ᥻"),
  bstack11l111_opy_ (u"ࠧࡪࡰࡷࡩࡳࡺࡁࡤࡶ࡬ࡳࡳ࠭᥼"), bstack11l111_opy_ (u"ࠨ࡫ࡱࡸࡪࡴࡴࡄࡣࡷࡩ࡬ࡵࡲࡺࠩ᥽"), bstack11l111_opy_ (u"ࠩ࡬ࡲࡹ࡫࡮ࡵࡈ࡯ࡥ࡬ࡹࠧ᥾"), bstack11l111_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡤࡰࡎࡴࡴࡦࡰࡷࡅࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭᥿"),
  bstack11l111_opy_ (u"ࠫࡩࡵ࡮ࡵࡕࡷࡳࡵࡇࡰࡱࡑࡱࡖࡪࡹࡥࡵࠩᦀ"),
  bstack11l111_opy_ (u"ࠬࡻ࡮ࡪࡥࡲࡨࡪࡑࡥࡺࡤࡲࡥࡷࡪࠧᦁ"), bstack11l111_opy_ (u"࠭ࡲࡦࡵࡨࡸࡐ࡫ࡹࡣࡱࡤࡶࡩ࠭ᦂ"),
  bstack11l111_opy_ (u"ࠧ࡯ࡱࡖ࡭࡬ࡴࠧᦃ"),
  bstack11l111_opy_ (u"ࠨ࡫ࡪࡲࡴࡸࡥࡖࡰ࡬ࡱࡵࡵࡲࡵࡣࡱࡸ࡛࡯ࡥࡸࡵࠪᦄ"),
  bstack11l111_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡲࡩࡸ࡯ࡪࡦ࡚ࡥࡹࡩࡨࡦࡴࡶࠫᦅ"),
  bstack11l111_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᦆ"),
  bstack11l111_opy_ (u"ࠫࡷ࡫ࡣࡳࡧࡤࡸࡪࡉࡨࡳࡱࡰࡩࡉࡸࡩࡷࡧࡵࡗࡪࡹࡳࡪࡱࡱࡷࠬᦇ"),
  bstack11l111_opy_ (u"ࠬࡴࡡࡵ࡫ࡹࡩ࡜࡫ࡢࡔࡥࡵࡩࡪࡴࡳࡩࡱࡷࠫᦈ"),
  bstack11l111_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࡓࡤࡴࡨࡩࡳࡹࡨࡰࡶࡓࡥࡹ࡮ࠧᦉ"),
  bstack11l111_opy_ (u"ࠧ࡯ࡧࡷࡻࡴࡸ࡫ࡔࡲࡨࡩࡩ࠭ᦊ"),
  bstack11l111_opy_ (u"ࠨࡩࡳࡷࡊࡴࡡࡣ࡮ࡨࡨࠬᦋ"),
  bstack11l111_opy_ (u"ࠩ࡬ࡷࡍ࡫ࡡࡥ࡮ࡨࡷࡸ࠭ᦌ"),
  bstack11l111_opy_ (u"ࠪࡥࡩࡨࡅࡹࡧࡦࡘ࡮ࡳࡥࡰࡷࡷࠫᦍ"),
  bstack11l111_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡨࡗࡨࡸࡩࡱࡶࠪᦎ"),
  bstack11l111_opy_ (u"ࠬࡹ࡫ࡪࡲࡇࡩࡻ࡯ࡣࡦࡋࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡥࡹ࡯࡯࡯ࠩᦏ"),
  bstack11l111_opy_ (u"࠭ࡡࡶࡶࡲࡋࡷࡧ࡮ࡵࡒࡨࡶࡲ࡯ࡳࡴ࡫ࡲࡲࡸ࠭ᦐ"),
  bstack11l111_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࡏࡣࡷࡹࡷࡧ࡬ࡐࡴ࡬ࡩࡳࡺࡡࡵ࡫ࡲࡲࠬᦑ"),
  bstack11l111_opy_ (u"ࠨࡵࡼࡷࡹ࡫࡭ࡑࡱࡵࡸࠬᦒ"),
  bstack11l111_opy_ (u"ࠩࡵࡩࡲࡵࡴࡦࡃࡧࡦࡍࡵࡳࡵࠩᦓ"),
  bstack11l111_opy_ (u"ࠪࡷࡰ࡯ࡰࡖࡰ࡯ࡳࡨࡱࠧᦔ"), bstack11l111_opy_ (u"ࠫࡺࡴ࡬ࡰࡥ࡮ࡘࡾࡶࡥࠨᦕ"), bstack11l111_opy_ (u"ࠬࡻ࡮࡭ࡱࡦ࡯ࡐ࡫ࡹࠨᦖ"),
  bstack11l111_opy_ (u"࠭ࡡࡶࡶࡲࡐࡦࡻ࡮ࡤࡪࠪᦗ"),
  bstack11l111_opy_ (u"ࠧࡴ࡭࡬ࡴࡑࡵࡧࡤࡣࡷࡇࡦࡶࡴࡶࡴࡨࠫᦘ"),
  bstack11l111_opy_ (u"ࠨࡷࡱ࡭ࡳࡹࡴࡢ࡮࡯ࡓࡹ࡮ࡥࡳࡒࡤࡧࡰࡧࡧࡦࡵࠪᦙ"),
  bstack11l111_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧ࡚࡭ࡳࡪ࡯ࡸࡃࡱ࡭ࡲࡧࡴࡪࡱࡱࠫᦚ"),
  bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡖࡲࡳࡱࡹࡖࡦࡴࡶ࡭ࡴࡴࠧᦛ"),
  bstack11l111_opy_ (u"ࠫࡪࡴࡦࡰࡴࡦࡩࡆࡶࡰࡊࡰࡶࡸࡦࡲ࡬ࠨᦜ"),
  bstack11l111_opy_ (u"ࠬ࡫࡮ࡴࡷࡵࡩ࡜࡫ࡢࡷ࡫ࡨࡻࡸࡎࡡࡷࡧࡓࡥ࡬࡫ࡳࠨᦝ"), bstack11l111_opy_ (u"࠭ࡷࡦࡤࡹ࡭ࡪࡽࡄࡦࡸࡷࡳࡴࡲࡳࡑࡱࡵࡸࠬᦞ"), bstack11l111_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡗࡦࡤࡹ࡭ࡪࡽࡄࡦࡶࡤ࡭ࡱࡹࡃࡰ࡮࡯ࡩࡨࡺࡩࡰࡰࠪᦟ"),
  bstack11l111_opy_ (u"ࠨࡴࡨࡱࡴࡺࡥࡂࡲࡳࡷࡈࡧࡣࡩࡧࡏ࡭ࡲ࡯ࡴࠨᦠ"),
  bstack11l111_opy_ (u"ࠩࡦࡥࡱ࡫࡮ࡥࡣࡵࡊࡴࡸ࡭ࡢࡶࠪᦡ"),
  bstack11l111_opy_ (u"ࠪࡦࡺࡴࡤ࡭ࡧࡌࡨࠬᦢ"),
  bstack11l111_opy_ (u"ࠫࡱࡧࡵ࡯ࡥ࡫ࡘ࡮ࡳࡥࡰࡷࡷࠫᦣ"),
  bstack11l111_opy_ (u"ࠬࡲ࡯ࡤࡣࡷ࡭ࡴࡴࡓࡦࡴࡹ࡭ࡨ࡫ࡳࡆࡰࡤࡦࡱ࡫ࡤࠨᦤ"), bstack11l111_opy_ (u"࠭࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࡔࡧࡵࡺ࡮ࡩࡥࡴࡃࡸࡸ࡭ࡵࡲࡪࡼࡨࡨࠬᦥ"),
  bstack11l111_opy_ (u"ࠧࡢࡷࡷࡳࡆࡩࡣࡦࡲࡷࡅࡱ࡫ࡲࡵࡵࠪᦦ"), bstack11l111_opy_ (u"ࠨࡣࡸࡸࡴࡊࡩࡴ࡯࡬ࡷࡸࡇ࡬ࡦࡴࡷࡷࠬᦧ"),
  bstack11l111_opy_ (u"ࠩࡱࡥࡹ࡯ࡶࡦࡋࡱࡷࡹࡸࡵ࡮ࡧࡱࡸࡸࡒࡩࡣࠩᦨ"),
  bstack11l111_opy_ (u"ࠪࡲࡦࡺࡩࡷࡧ࡚ࡩࡧ࡚ࡡࡱࠩᦩ"),
  bstack11l111_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࡍࡳ࡯ࡴࡪࡣ࡯࡙ࡷࡲࠧᦪ"), bstack11l111_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࡆࡲ࡬ࡰࡹࡓࡳࡵࡻࡰࡴࠩᦫ"), bstack11l111_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮ࡏࡧ࡯ࡱࡵࡩࡋࡸࡡࡶࡦ࡚ࡥࡷࡴࡩ࡯ࡩࠪ᦬"), bstack11l111_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࡏࡱࡧࡱࡐ࡮ࡴ࡫ࡴࡋࡱࡆࡦࡩ࡫ࡨࡴࡲࡹࡳࡪࠧ᦭"),
  bstack11l111_opy_ (u"ࠨ࡭ࡨࡩࡵࡑࡥࡺࡅ࡫ࡥ࡮ࡴࡳࠨ᦮"),
  bstack11l111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡪࡼࡤࡦࡱ࡫ࡓࡵࡴ࡬ࡲ࡬ࡹࡄࡪࡴࠪ᦯"),
  bstack11l111_opy_ (u"ࠪࡴࡷࡵࡣࡦࡵࡶࡅࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᦰ"),
  bstack11l111_opy_ (u"ࠫ࡮ࡴࡴࡦࡴࡎࡩࡾࡊࡥ࡭ࡣࡼࠫᦱ"),
  bstack11l111_opy_ (u"ࠬࡹࡨࡰࡹࡌࡓࡘࡒ࡯ࡨࠩᦲ"),
  bstack11l111_opy_ (u"࠭ࡳࡦࡰࡧࡏࡪࡿࡓࡵࡴࡤࡸࡪ࡭ࡹࠨᦳ"),
  bstack11l111_opy_ (u"ࠧࡸࡧࡥ࡯࡮ࡺࡒࡦࡵࡳࡳࡳࡹࡥࡕ࡫ࡰࡩࡴࡻࡴࠨᦴ"), bstack11l111_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸ࡜ࡧࡩࡵࡖ࡬ࡱࡪࡵࡵࡵࠩᦵ"),
  bstack11l111_opy_ (u"ࠩࡵࡩࡲࡵࡴࡦࡆࡨࡦࡺ࡭ࡐࡳࡱࡻࡽࠬᦶ"),
  bstack11l111_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡄࡷࡾࡴࡣࡆࡺࡨࡧࡺࡺࡥࡇࡴࡲࡱࡍࡺࡴࡱࡵࠪᦷ"),
  bstack11l111_opy_ (u"ࠫࡸࡱࡩࡱࡎࡲ࡫ࡈࡧࡰࡵࡷࡵࡩࠬᦸ"),
  bstack11l111_opy_ (u"ࠬࡽࡥࡣ࡭࡬ࡸࡉ࡫ࡢࡶࡩࡓࡶࡴࡾࡹࡑࡱࡵࡸࠬᦹ"),
  bstack11l111_opy_ (u"࠭ࡦࡶ࡮࡯ࡇࡴࡴࡴࡦࡺࡷࡐ࡮ࡹࡴࠨᦺ"),
  bstack11l111_opy_ (u"ࠧࡸࡣ࡬ࡸࡋࡵࡲࡂࡲࡳࡗࡨࡸࡩࡱࡶࠪᦻ"),
  bstack11l111_opy_ (u"ࠨࡹࡨࡦࡻ࡯ࡥࡸࡅࡲࡲࡳ࡫ࡣࡵࡔࡨࡸࡷ࡯ࡥࡴࠩᦼ"),
  bstack11l111_opy_ (u"ࠩࡤࡴࡵࡔࡡ࡮ࡧࠪᦽ"),
  bstack11l111_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡖࡗࡑࡉࡥࡳࡶࠪᦾ"),
  bstack11l111_opy_ (u"ࠫࡹࡧࡰࡘ࡫ࡷ࡬ࡘ࡮࡯ࡳࡶࡓࡶࡪࡹࡳࡅࡷࡵࡥࡹ࡯࡯࡯ࠩᦿ"),
  bstack11l111_opy_ (u"ࠬࡹࡣࡢ࡮ࡨࡊࡦࡩࡴࡰࡴࠪᧀ"),
  bstack11l111_opy_ (u"࠭ࡷࡥࡣࡏࡳࡨࡧ࡬ࡑࡱࡵࡸࠬᧁ"),
  bstack11l111_opy_ (u"ࠧࡴࡪࡲࡻ࡝ࡩ࡯ࡥࡧࡏࡳ࡬࠭ᧂ"),
  bstack11l111_opy_ (u"ࠨ࡫ࡲࡷࡎࡴࡳࡵࡣ࡯ࡰࡕࡧࡵࡴࡧࠪᧃ"),
  bstack11l111_opy_ (u"ࠩࡻࡧࡴࡪࡥࡄࡱࡱࡪ࡮࡭ࡆࡪ࡮ࡨࠫᧄ"),
  bstack11l111_opy_ (u"ࠪ࡯ࡪࡿࡣࡩࡣ࡬ࡲࡕࡧࡳࡴࡹࡲࡶࡩ࠭ᧅ"),
  bstack11l111_opy_ (u"ࠫࡺࡹࡥࡑࡴࡨࡦࡺ࡯࡬ࡵ࡙ࡇࡅࠬᧆ"),
  bstack11l111_opy_ (u"ࠬࡶࡲࡦࡸࡨࡲࡹ࡝ࡄࡂࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠭ᧇ"),
  bstack11l111_opy_ (u"࠭ࡷࡦࡤࡇࡶ࡮ࡼࡥࡳࡃࡪࡩࡳࡺࡕࡳ࡮ࠪᧈ"),
  bstack11l111_opy_ (u"ࠧ࡬ࡧࡼࡧ࡭ࡧࡩ࡯ࡒࡤࡸ࡭࠭ᧉ"),
  bstack11l111_opy_ (u"ࠨࡷࡶࡩࡓ࡫ࡷࡘࡆࡄࠫ᧊"),
  bstack11l111_opy_ (u"ࠩࡺࡨࡦࡒࡡࡶࡰࡦ࡬࡙࡯࡭ࡦࡱࡸࡸࠬ᧋"), bstack11l111_opy_ (u"ࠪࡻࡩࡧࡃࡰࡰࡱࡩࡨࡺࡩࡰࡰࡗ࡭ࡲ࡫࡯ࡶࡶࠪ᧌"),
  bstack11l111_opy_ (u"ࠫࡽࡩ࡯ࡥࡧࡒࡶ࡬ࡏࡤࠨ᧍"), bstack11l111_opy_ (u"ࠬࡾࡣࡰࡦࡨࡗ࡮࡭࡮ࡪࡰࡪࡍࡩ࠭᧎"),
  bstack11l111_opy_ (u"࠭ࡵࡱࡦࡤࡸࡪࡪࡗࡅࡃࡅࡹࡳࡪ࡬ࡦࡋࡧࠫ᧏"),
  bstack11l111_opy_ (u"ࠧࡳࡧࡶࡩࡹࡕ࡮ࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡶࡹࡕ࡮࡭ࡻࠪ᧐"),
  bstack11l111_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡖ࡬ࡱࡪࡵࡵࡵࡵࠪ᧑"),
  bstack11l111_opy_ (u"ࠩࡺࡨࡦ࡙ࡴࡢࡴࡷࡹࡵࡘࡥࡵࡴ࡬ࡩࡸ࠭᧒"), bstack11l111_opy_ (u"ࠪࡻࡩࡧࡓࡵࡣࡵࡸࡺࡶࡒࡦࡶࡵࡽࡎࡴࡴࡦࡴࡹࡥࡱ࠭᧓"),
  bstack11l111_opy_ (u"ࠫࡨࡵ࡮࡯ࡧࡦࡸࡍࡧࡲࡥࡹࡤࡶࡪࡑࡥࡺࡤࡲࡥࡷࡪࠧ᧔"),
  bstack11l111_opy_ (u"ࠬࡳࡡࡹࡖࡼࡴ࡮ࡴࡧࡇࡴࡨࡵࡺ࡫࡮ࡤࡻࠪ᧕"),
  bstack11l111_opy_ (u"࠭ࡳࡪ࡯ࡳࡰࡪࡏࡳࡗ࡫ࡶ࡭ࡧࡲࡥࡄࡪࡨࡧࡰ࠭᧖"),
  bstack11l111_opy_ (u"ࠧࡶࡵࡨࡇࡦࡸࡴࡩࡣࡪࡩࡘࡹ࡬ࠨ᧗"),
  bstack11l111_opy_ (u"ࠨࡵ࡫ࡳࡺࡲࡤࡖࡵࡨࡗ࡮ࡴࡧ࡭ࡧࡷࡳࡳ࡚ࡥࡴࡶࡐࡥࡳࡧࡧࡦࡴࠪ᧘"),
  bstack11l111_opy_ (u"ࠩࡶࡸࡦࡸࡴࡊ࡙ࡇࡔࠬ᧙"),
  bstack11l111_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡖࡲࡹࡨ࡮ࡉࡥࡇࡱࡶࡴࡲ࡬ࠨ᧚"),
  bstack11l111_opy_ (u"ࠫ࡮࡭࡮ࡰࡴࡨࡌ࡮ࡪࡤࡦࡰࡄࡴ࡮ࡖ࡯࡭࡫ࡦࡽࡊࡸࡲࡰࡴࠪ᧛"),
  bstack11l111_opy_ (u"ࠬࡳ࡯ࡤ࡭ࡏࡳࡨࡧࡴࡪࡱࡱࡅࡵࡶࠧ᧜"),
  bstack11l111_opy_ (u"࠭࡬ࡰࡩࡦࡥࡹࡌ࡯ࡳ࡯ࡤࡸࠬ᧝"), bstack11l111_opy_ (u"ࠧ࡭ࡱࡪࡧࡦࡺࡆࡪ࡮ࡷࡩࡷ࡙ࡰࡦࡥࡶࠫ᧞"),
  bstack11l111_opy_ (u"ࠨࡣ࡯ࡰࡴࡽࡄࡦ࡮ࡤࡽࡆࡪࡢࠨ᧟"),
  bstack11l111_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡌࡨࡑࡵࡣࡢࡶࡲࡶࡆࡻࡴࡰࡥࡲࡱࡵࡲࡥࡵ࡫ࡲࡲࠬ᧠")
]
bstack11l1l1lll_opy_ = bstack11l111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡦࡶࡩ࠮ࡥ࡯ࡳࡺࡪ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦ࠱ࡸࡴࡱࡵࡡࡥࠩ᧡")
bstack1llll1l11l_opy_ = [bstack11l111_opy_ (u"ࠫ࠳ࡧࡰ࡬ࠩ᧢"), bstack11l111_opy_ (u"ࠬ࠴ࡡࡢࡤࠪ᧣"), bstack11l111_opy_ (u"࠭࠮ࡪࡲࡤࠫ᧤")]
bstack1ll1l1ll1_opy_ = [bstack11l111_opy_ (u"ࠧࡪࡦࠪ᧥"), bstack11l111_opy_ (u"ࠨࡲࡤࡸ࡭࠭᧦"), bstack11l111_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡡ࡬ࡨࠬ᧧"), bstack11l111_opy_ (u"ࠪࡷ࡭ࡧࡲࡦࡣࡥࡰࡪࡥࡩࡥࠩ᧨")]
bstack11111llll_opy_ = {
  bstack11l111_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ᧩"): bstack11l111_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ᧪"),
  bstack11l111_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧ᧫"): bstack11l111_opy_ (u"ࠧ࡮ࡱࡽ࠾࡫࡯ࡲࡦࡨࡲࡼࡔࡶࡴࡪࡱࡱࡷࠬ᧬"),
  bstack11l111_opy_ (u"ࠨࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭᧭"): bstack11l111_opy_ (u"ࠩࡰࡷ࠿࡫ࡤࡨࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ᧮"),
  bstack11l111_opy_ (u"ࠪ࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭᧯"): bstack11l111_opy_ (u"ࠫࡸ࡫࠺ࡪࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ᧰"),
  bstack11l111_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࡔࡶࡴࡪࡱࡱࡷࠬ᧱"): bstack11l111_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧ᧲")
}
bstack1l11l11111_opy_ = [
  bstack11l111_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ᧳"),
  bstack11l111_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭᧴"),
  bstack11l111_opy_ (u"ࠩࡰࡷ࠿࡫ࡤࡨࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ᧵"),
  bstack11l111_opy_ (u"ࠪࡷࡪࡀࡩࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᧶"),
  bstack11l111_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬ᧷"),
]
bstack1111l1ll1_opy_ = bstack11lll11111_opy_ + bstack11l11ll1l11_opy_ + bstack1l111ll1l1_opy_
bstack1l1111111_opy_ = [
  bstack11l111_opy_ (u"ࠬࡤ࡬ࡰࡥࡤࡰ࡭ࡵࡳࡵࠦࠪ᧸"),
  bstack11l111_opy_ (u"࠭࡞ࡣࡵ࠰ࡰࡴࡩࡡ࡭࠰ࡦࡳࡲࠪࠧ᧹"),
  bstack11l111_opy_ (u"ࠧ࡟࠳࠵࠻࠳࠭᧺"),
  bstack11l111_opy_ (u"ࠨࡠ࠴࠴࠳࠭᧻"),
  bstack11l111_opy_ (u"ࠩࡡ࠵࠼࠸࠮࠲࡝࠹࠱࠾ࡣ࠮ࠨ᧼"),
  bstack11l111_opy_ (u"ࠪࡢ࠶࠽࠲࠯࠴࡞࠴࠲࠿࡝࠯ࠩ᧽"),
  bstack11l111_opy_ (u"ࠫࡣ࠷࠷࠳࠰࠶࡟࠵࠳࠱࡞࠰ࠪ᧾"),
  bstack11l111_opy_ (u"ࠬࡤ࠱࠺࠴࠱࠵࠻࠾࠮ࠨ᧿")
]
bstack11l1l1l1l11_opy_ = bstack11l111_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡢࡲ࡬࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧᨀ")
bstack1l11111lll_opy_ = bstack11l111_opy_ (u"ࠧࡴࡦ࡮࠳ࡻ࠷࠯ࡦࡸࡨࡲࡹ࠭ᨁ")
bstack11111l111_opy_ = [ bstack11l111_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪᨂ") ]
bstack1l11l11ll_opy_ = [ bstack11l111_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨᨃ") ]
bstack1ll111111_opy_ = [bstack11l111_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧᨄ")]
bstack1l1llllll1_opy_ = [ bstack11l111_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫᨅ") ]
bstack1l1l11l1ll_opy_ = bstack11l111_opy_ (u"࡙ࠬࡄࡌࡕࡨࡸࡺࡶࠧᨆ")
bstack11ll11ll1l_opy_ = bstack11l111_opy_ (u"࠭ࡓࡅࡍࡗࡩࡸࡺࡁࡵࡶࡨࡱࡵࡺࡥࡥࠩᨇ")
bstack11l1ll1l1l_opy_ = bstack11l111_opy_ (u"ࠧࡔࡆࡎࡘࡪࡹࡴࡔࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࠫᨈ")
bstack11l11ll111_opy_ = bstack11l111_opy_ (u"ࠨ࠶࠱࠴࠳࠶ࠧᨉ")
bstack1l11l11l1_opy_ = [
  bstack11l111_opy_ (u"ࠩࡈࡖࡗࡥࡆࡂࡋࡏࡉࡉ࠭ᨊ"),
  bstack11l111_opy_ (u"ࠪࡉࡗࡘ࡟ࡕࡋࡐࡉࡉࡥࡏࡖࡖࠪᨋ"),
  bstack11l111_opy_ (u"ࠫࡊࡘࡒࡠࡄࡏࡓࡈࡑࡅࡅࡡࡅ࡝ࡤࡉࡌࡊࡇࡑࡘࠬᨌ"),
  bstack11l111_opy_ (u"ࠬࡋࡒࡓࡡࡑࡉ࡙࡝ࡏࡓࡍࡢࡇࡍࡇࡎࡈࡇࡇࠫᨍ"),
  bstack11l111_opy_ (u"࠭ࡅࡓࡔࡢࡗࡔࡉࡋࡆࡖࡢࡒࡔ࡚࡟ࡄࡑࡑࡒࡊࡉࡔࡆࡆࠪᨎ"),
  bstack11l111_opy_ (u"ࠧࡆࡔࡕࡣࡈࡕࡎࡏࡇࡆࡘࡎࡕࡎࡠࡅࡏࡓࡘࡋࡄࠨᨏ"),
  bstack11l111_opy_ (u"ࠨࡇࡕࡖࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡕࡉࡘࡋࡔࠨᨐ"),
  bstack11l111_opy_ (u"ࠩࡈࡖࡗࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡖࡊࡌࡕࡔࡇࡇࠫᨑ"),
  bstack11l111_opy_ (u"ࠪࡉࡗࡘ࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣࡆࡈࡏࡓࡖࡈࡈࠬᨒ"),
  bstack11l111_opy_ (u"ࠫࡊࡘࡒࡠࡅࡒࡒࡓࡋࡃࡕࡋࡒࡒࡤࡌࡁࡊࡎࡈࡈࠬᨓ"),
  bstack11l111_opy_ (u"ࠬࡋࡒࡓࡡࡑࡅࡒࡋ࡟ࡏࡑࡗࡣࡗࡋࡓࡐࡎ࡙ࡉࡉ࠭ᨔ"),
  bstack11l111_opy_ (u"࠭ࡅࡓࡔࡢࡅࡉࡊࡒࡆࡕࡖࡣࡎࡔࡖࡂࡎࡌࡈࠬᨕ"),
  bstack11l111_opy_ (u"ࠧࡆࡔࡕࡣࡆࡊࡄࡓࡇࡖࡗࡤ࡛ࡎࡓࡇࡄࡇࡍࡇࡂࡍࡇࠪᨖ"),
  bstack11l111_opy_ (u"ࠨࡇࡕࡖࡤ࡚ࡕࡏࡐࡈࡐࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡉࡅࡎࡒࡅࡅࠩᨗ"),
  bstack11l111_opy_ (u"ࠩࡈࡖࡗࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡘࡎࡓࡅࡅࡡࡒ࡙࡙ᨘ࠭"),
  bstack11l111_opy_ (u"ࠪࡉࡗࡘ࡟ࡔࡑࡆࡏࡘࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡊࡆࡏࡌࡆࡆࠪᨙ"),
  bstack11l111_opy_ (u"ࠫࡊࡘࡒࡠࡕࡒࡇࡐ࡙࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣࡍࡕࡓࡕࡡࡘࡒࡗࡋࡁࡄࡊࡄࡆࡑࡋࠧᨚ"),
  bstack11l111_opy_ (u"ࠬࡋࡒࡓࡡࡓࡖࡔ࡞࡙ࡠࡅࡒࡒࡓࡋࡃࡕࡋࡒࡒࡤࡌࡁࡊࡎࡈࡈࠬᨛ"),
  bstack11l111_opy_ (u"࠭ࡅࡓࡔࡢࡒࡆࡓࡅࡠࡐࡒࡘࡤࡘࡅࡔࡑࡏ࡚ࡊࡊࠧ᨜"),
  bstack11l111_opy_ (u"ࠧࡆࡔࡕࡣࡓࡇࡍࡆࡡࡕࡉࡘࡕࡌࡖࡖࡌࡓࡓࡥࡆࡂࡋࡏࡉࡉ࠭᨝"),
  bstack11l111_opy_ (u"ࠨࡇࡕࡖࡤࡓࡁࡏࡆࡄࡘࡔࡘ࡙ࡠࡒࡕࡓ࡝࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟ࡇࡃࡌࡐࡊࡊࠧ᨞"),
]
bstack11lll11l11_opy_ = bstack11l111_opy_ (u"ࠩ࠱࠳ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡥࡷࡺࡩࡧࡣࡦࡸࡸ࠵ࠧ᨟")
bstack11111l11ll_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠪࢂࠬᨠ")), bstack11l111_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᨡ"), bstack11l111_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫᨢ"))
bstack11l11lll11l_opy_ = bstack11l111_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡥࡵ࡯ࠧᨣ")
bstack11l11ll1lll_opy_ = [ bstack11l111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧᨤ"), bstack11l111_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧᨥ"), bstack11l111_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨᨦ"), bstack11l111_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪᨧ")]
bstack111ll11l11_opy_ = [ bstack11l111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᨨ"), bstack11l111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫᨩ"), bstack11l111_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬᨪ"), bstack11l111_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧᨫ") ]
bstack1lll1l11ll_opy_ = [ bstack11l111_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧᨬ") ]
bstack11l11llll1l_opy_ = [ bstack11l111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩᨭ") ]
bstack1ll1l11111_opy_ = 360
bstack11ll11l1ll1_opy_ = bstack11l111_opy_ (u"ࠥࡥࡵࡶ࠭ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠥᨮ")
bstack11l1l11ll1l_opy_ = bstack11l111_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡡࡱ࡫࠲ࡺ࠶࠵ࡩࡴࡵࡸࡩࡸࠨᨯ")
bstack11l1l1l1111_opy_ = bstack11l111_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫࠯ࡢࡲ࡬࠳ࡻ࠷࠯ࡪࡵࡶࡹࡪࡹ࠭ࡴࡷࡰࡱࡦࡸࡹࠣᨰ")
bstack11l1l1l111l_opy_ = bstack11l111_opy_ (u"ࠨࡁࡱࡲࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡵࡧࡶࡸࡸࠦࡡࡳࡧࠣࡷࡺࡶࡰࡰࡴࡷࡩࡩࠦ࡯࡯ࠢࡒࡗࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࠥࡴࠢࡤࡲࡩࠦࡡࡣࡱࡹࡩࠥ࡬࡯ࡳࠢࡄࡲࡩࡸ࡯ࡪࡦࠣࡨࡪࡼࡩࡤࡧࡶ࠲ࠧᨱ")
bstack11l1l11l1l1_opy_ = bstack11l111_opy_ (u"ࠢ࠲࠳࠱࠴ࠧᨲ")
bstack1ll1llll_opy_ = {
  bstack11l111_opy_ (u"ࠨࡒࡄࡗࡘ࠭ᨳ"): bstack11l111_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᨴ"),
  bstack11l111_opy_ (u"ࠪࡊࡆࡏࡌࠨᨵ"): bstack11l111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᨶ"),
  bstack11l111_opy_ (u"࡙ࠬࡋࡊࡒࠪᨷ"): bstack11l111_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᨸ")
}
bstack11l11111ll_opy_ = [
  bstack11l111_opy_ (u"ࠢࡨࡧࡷࠦᨹ"),
  bstack11l111_opy_ (u"ࠣࡩࡲࡆࡦࡩ࡫ࠣᨺ"),
  bstack11l111_opy_ (u"ࠤࡪࡳࡋࡵࡲࡸࡣࡵࡨࠧᨻ"),
  bstack11l111_opy_ (u"ࠥࡶࡪ࡬ࡲࡦࡵ࡫ࠦᨼ"),
  bstack11l111_opy_ (u"ࠦࡨࡲࡩࡤ࡭ࡈࡰࡪࡳࡥ࡯ࡶࠥᨽ"),
  bstack11l111_opy_ (u"ࠧࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠤᨾ"),
  bstack11l111_opy_ (u"ࠨࡳࡶࡤࡰ࡭ࡹࡋ࡬ࡦ࡯ࡨࡲࡹࠨᨿ"),
  bstack11l111_opy_ (u"ࠢࡴࡧࡱࡨࡐ࡫ࡹࡴࡖࡲࡉࡱ࡫࡭ࡦࡰࡷࠦᩀ"),
  bstack11l111_opy_ (u"ࠣࡵࡨࡲࡩࡑࡥࡺࡵࡗࡳࡆࡩࡴࡪࡸࡨࡉࡱ࡫࡭ࡦࡰࡷࠦᩁ"),
  bstack11l111_opy_ (u"ࠤࡦࡰࡪࡧࡲࡆ࡮ࡨࡱࡪࡴࡴࠣᩂ"),
  bstack11l111_opy_ (u"ࠥࡥࡨࡺࡩࡰࡰࡶࠦᩃ"),
  bstack11l111_opy_ (u"ࠦࡪࡾࡥࡤࡷࡷࡩࡘࡩࡲࡪࡲࡷࠦᩄ"),
  bstack11l111_opy_ (u"ࠧ࡫ࡸࡦࡥࡸࡸࡪࡇࡳࡺࡰࡦࡗࡨࡸࡩࡱࡶࠥᩅ"),
  bstack11l111_opy_ (u"ࠨࡣ࡭ࡱࡶࡩࠧᩆ"),
  bstack11l111_opy_ (u"ࠢࡲࡷ࡬ࡸࠧᩇ"),
  bstack11l111_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡖࡲࡹࡨ࡮ࡁࡤࡶ࡬ࡳࡳࠨᩈ"),
  bstack11l111_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡐࡹࡱࡺࡩࡕࡱࡸࡧ࡭ࠨᩉ"),
  bstack11l111_opy_ (u"ࠥࡷ࡭ࡧ࡫ࡦࠤᩊ"),
  bstack11l111_opy_ (u"ࠦࡨࡲ࡯ࡴࡧࡄࡴࡵࠨᩋ")
]
bstack11l1l1111ll_opy_ = [
  bstack11l111_opy_ (u"ࠧࡩ࡬ࡪࡥ࡮ࠦᩌ"),
  bstack11l111_opy_ (u"ࠨࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠥᩍ"),
  bstack11l111_opy_ (u"ࠢࡢࡷࡷࡳࠧᩎ"),
  bstack11l111_opy_ (u"ࠣ࡯ࡤࡲࡺࡧ࡬ࠣᩏ"),
  bstack11l111_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦᩐ")
]
bstack1lll111111_opy_ = {
  bstack11l111_opy_ (u"ࠥࡧࡱ࡯ࡣ࡬ࠤᩑ"): [bstack11l111_opy_ (u"ࠦࡨࡲࡩࡤ࡭ࡈࡰࡪࡳࡥ࡯ࡶࠥᩒ")],
  bstack11l111_opy_ (u"ࠧࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠤᩓ"): [bstack11l111_opy_ (u"ࠨࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠥᩔ")],
  bstack11l111_opy_ (u"ࠢࡢࡷࡷࡳࠧᩕ"): [bstack11l111_opy_ (u"ࠣࡵࡨࡲࡩࡑࡥࡺࡵࡗࡳࡊࡲࡥ࡮ࡧࡱࡸࠧᩖ"), bstack11l111_opy_ (u"ࠤࡶࡩࡳࡪࡋࡦࡻࡶࡘࡴࡇࡣࡵ࡫ࡹࡩࡊࡲࡥ࡮ࡧࡱࡸࠧᩗ"), bstack11l111_opy_ (u"ࠥࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠢᩘ"), bstack11l111_opy_ (u"ࠦࡨࡲࡩࡤ࡭ࡈࡰࡪࡳࡥ࡯ࡶࠥᩙ")],
  bstack11l111_opy_ (u"ࠧࡳࡡ࡯ࡷࡤࡰࠧᩚ"): [bstack11l111_opy_ (u"ࠨ࡭ࡢࡰࡸࡥࡱࠨᩛ")],
  bstack11l111_opy_ (u"ࠢࡵࡧࡶࡸࡨࡧࡳࡦࠤᩜ"): [bstack11l111_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥᩝ")],
}
bstack11l11lll111_opy_ = {
  bstack11l111_opy_ (u"ࠤࡦࡰ࡮ࡩ࡫ࡆ࡮ࡨࡱࡪࡴࡴࠣᩞ"): bstack11l111_opy_ (u"ࠥࡧࡱ࡯ࡣ࡬ࠤ᩟"),
  bstack11l111_opy_ (u"ࠦࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴ᩠ࠣ"): bstack11l111_opy_ (u"ࠧࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠤᩡ"),
  bstack11l111_opy_ (u"ࠨࡳࡦࡰࡧࡏࡪࡿࡳࡕࡱࡈࡰࡪࡳࡥ࡯ࡶࠥᩢ"): bstack11l111_opy_ (u"ࠢࡴࡧࡱࡨࡐ࡫ࡹࡴࠤᩣ"),
  bstack11l111_opy_ (u"ࠣࡵࡨࡲࡩࡑࡥࡺࡵࡗࡳࡆࡩࡴࡪࡸࡨࡉࡱ࡫࡭ࡦࡰࡷࠦᩤ"): bstack11l111_opy_ (u"ࠤࡶࡩࡳࡪࡋࡦࡻࡶࠦᩥ"),
  bstack11l111_opy_ (u"ࠥࡸࡪࡹࡴࡤࡣࡶࡩࠧᩦ"): bstack11l111_opy_ (u"ࠦࡹ࡫ࡳࡵࡥࡤࡷࡪࠨᩧ")
}
bstack1l1ll111_opy_ = {
  bstack11l111_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩᩨ"): bstack11l111_opy_ (u"࠭ࡓࡶ࡫ࡷࡩ࡙ࠥࡥࡵࡷࡳࠫᩩ"),
  bstack11l111_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡁࡍࡎࠪᩪ"): bstack11l111_opy_ (u"ࠨࡕࡸ࡭ࡹ࡫ࠠࡕࡧࡤࡶࡩࡵࡷ࡯ࠩᩫ"),
  bstack11l111_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᩬ"): bstack11l111_opy_ (u"ࠪࡘࡪࡹࡴࠡࡕࡨࡸࡺࡶࠧᩭ"),
  bstack11l111_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠨᩮ"): bstack11l111_opy_ (u"࡚ࠬࡥࡴࡶࠣࡘࡪࡧࡲࡥࡱࡺࡲࠬᩯ")
}
bstack11l11ll11l1_opy_ = 65536
bstack11l1l11llll_opy_ = bstack11l111_opy_ (u"࠭࠮࠯࠰࡞ࡘࡗ࡛ࡎࡄࡃࡗࡉࡉࡣࠧᩰ")
bstack11l11ll11ll_opy_ = [
      bstack11l111_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩᩱ"), bstack11l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫᩲ"), bstack11l111_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬᩳ"), bstack11l111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧᩴ"), bstack11l111_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸ࠭᩵"),
      bstack11l111_opy_ (u"ࠬࡶࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨ᩶"), bstack11l111_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡧࡳࡴࠩ᩷"), bstack11l111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡖࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨ᩸"), bstack11l111_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡐࡳࡱࡻࡽࡕࡧࡳࡴࠩ᩹"),
      bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ᩺"), bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ᩻"), bstack11l111_opy_ (u"ࠫࡦࡻࡴࡩࡖࡲ࡯ࡪࡴࠧ᩼")
    ]
bstack11l11l1llll_opy_= {
  bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ᩽"): bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ᩾"),
  bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶ᩿ࠫ"): bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ᪀"),
  bstack11l111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ᪁"): bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ᪂"),
  bstack11l111_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ᪃"): bstack11l111_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ᪄"),
  bstack11l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ᪅"): bstack11l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ᪆"),
  bstack11l111_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪ᪇"): bstack11l111_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫ᪈"),
  bstack11l111_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭᪉"): bstack11l111_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧ᪊"),
  bstack11l111_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ᪋"): bstack11l111_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ᪌"),
  bstack11l111_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ᪍"): bstack11l111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ᪎"),
  bstack11l111_opy_ (u"ࠩࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠧ᪏"): bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠨ᪐"),
  bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ᪑"): bstack11l111_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ᪒"),
  bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡖࡪࡶ࡯ࡳࡶ࡬ࡲ࡬࠭᪓"): bstack11l111_opy_ (u"ࠧࡵࡧࡶࡸࡗ࡫ࡰࡰࡴࡷ࡭ࡳ࡭ࠧ᪔"),
  bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ᪕"): bstack11l111_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭᪖"),
  bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡓࡧࡳࡳࡷࡺࡩ࡯ࡩࡒࡴࡹ࡯࡯࡯ࡵࠪ᪗"): bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡔࡨࡴࡴࡸࡴࡪࡰࡪࡓࡵࡺࡩࡰࡰࡶࠫ᪘"),
  bstack11l111_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱ࡛ࡧࡲࡪࡣࡥࡰࡪࡹࠧ᪙"): bstack11l111_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠨ᪚"),
  bstack11l111_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ᪛"): bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪ᪜"),
  bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ᪝"): bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ᪞"),
  bstack11l111_opy_ (u"ࠫࡷ࡫ࡲࡶࡰࡗࡩࡸࡺࡳࠨ᪟"): bstack11l111_opy_ (u"ࠬࡸࡥࡳࡷࡱࡘࡪࡹࡴࡴࠩ᪠"),
  bstack11l111_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ᪡"): bstack11l111_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭᪢"),
  bstack11l111_opy_ (u"ࠨࡲࡨࡶࡨࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ᪣"): bstack11l111_opy_ (u"ࠩࡳࡩࡷࡩࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ᪤"),
  bstack11l111_opy_ (u"ࠪࡴࡪࡸࡣࡺࡅࡤࡴࡹࡻࡲࡦࡏࡲࡨࡪ࠭᪥"): bstack11l111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡆࡥࡵࡺࡵࡳࡧࡐࡳࡩ࡫ࠧ᪦"),
  bstack11l111_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡇࡵࡵࡱࡆࡥࡵࡺࡵࡳࡧࡏࡳ࡬ࡹࠧᪧ"): bstack11l111_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁࡶࡶࡲࡇࡦࡶࡴࡶࡴࡨࡐࡴ࡭ࡳࠨ᪨"),
  bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ᪩"): bstack11l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ᪪"),
  bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᪫"): bstack11l111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ᪬"),
  bstack11l111_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ᪭"): bstack11l111_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ᪮"),
  bstack11l111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ᪯"): bstack11l111_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࡓࡵࡺࡩࡰࡰࡶࠫ᪰"),
  bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡔࡶࡴࡪࡱࡱࡷࠬ᪱"): bstack11l111_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭᪲"),
  bstack11l111_opy_ (u"ࠪࡴࡷࡵࡸࡺࡕࡨࡸࡹ࡯࡮ࡨࡵࠪ᪳"): bstack11l111_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡖࡩࡹࡺࡩ࡯ࡩࡶࠫ᪴")
}
bstack11l1l1111l1_opy_ = [bstack11l111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ᪵ࠬ"), bstack11l111_opy_ (u"࠭ࡲࡰࡤࡲࡸ᪶ࠬ")]
bstack1l1lllll11_opy_ = (bstack11l111_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ᪷ࠢ"),)
bstack11l11lll1l1_opy_ = bstack11l111_opy_ (u"ࠨࡵࡧ࡯࠴ࡼ࠱࠰ࡷࡳࡨࡦࡺࡥࡠࡥ࡯࡭᪸ࠬ")
bstack1l111lll1_opy_ = bstack11l111_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡵ࡯࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠲ࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦ࠱ࡹ࠵࠴࡭ࡲࡪࡦࡶ࠳᪹ࠧ")
bstack1l1l1ll11l_opy_ = bstack11l111_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳࡬ࡸࡩࡥ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡪࡡࡴࡪࡥࡳࡦࡸࡤ࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࠤ᪺")
bstack111ll111l_opy_ = bstack11l111_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡧࡵࡵࡱࡰࡥࡹ࡫࠭ࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨ࠳ࡻ࠷࠯ࡣࡷ࡬ࡰࡩࡹ࠮࡫ࡵࡲࡲࠧ᪻")
class EVENTS(Enum):
  bstack11l11l1l1ll_opy_ = bstack11l111_opy_ (u"ࠬࡹࡤ࡬࠼ࡲ࠵࠶ࡿ࠺ࡱࡴ࡬ࡲࡹ࠳ࡢࡶ࡫࡯ࡨࡱ࡯࡮࡬ࠩ᪼")
  bstack11l111ll1_opy_ = bstack11l111_opy_ (u"࠭ࡳࡥ࡭࠽ࡧࡱ࡫ࡡ࡯ࡷࡳ᪽ࠫ") # final bstack11l1l11111l_opy_
  bstack11l11l1l1l1_opy_ = bstack11l111_opy_ (u"ࠧࡴࡦ࡮࠾ࡸ࡫࡮ࡥ࡮ࡲ࡫ࡸ࠭᪾")
  bstack11llll11ll_opy_ = bstack11l111_opy_ (u"ࠨࡵࡧ࡯࠿ࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦ࠼ࡳࡶ࡮ࡴࡴ࠮ࡤࡸ࡭ࡱࡪ࡬ࡪࡰ࡮ᪿࠫ") #shift post bstack11l1l1l11l1_opy_
  bstack1l1lll1l1l_opy_ = bstack11l111_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡥ࠻ࡲࡵ࡭ࡳࡺ࠭ࡣࡷ࡬ࡰࡩࡲࡩ࡯࡭ᫀࠪ") #shift post bstack11l1l1l11l1_opy_
  bstack11l11l1lll1_opy_ = bstack11l111_opy_ (u"ࠪࡷࡩࡱ࠺ࡵࡧࡶࡸ࡭ࡻࡢࠨ᫁") #shift
  bstack11l11ll1l1l_opy_ = bstack11l111_opy_ (u"ࠫࡸࡪ࡫࠻ࡲࡨࡶࡨࡿ࠺ࡥࡱࡺࡲࡱࡵࡡࡥࠩ᫂") #shift
  bstack1l1ll1l11_opy_ = bstack11l111_opy_ (u"ࠬࡹࡤ࡬࠼ࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪࡀࡨࡶࡤ࠰ࡱࡦࡴࡡࡨࡧࡰࡩࡳࡺ᫃ࠧ")
  bstack1l111ll1111_opy_ = bstack11l111_opy_ (u"࠭ࡳࡥ࡭࠽ࡥ࠶࠷ࡹ࠻ࡵࡤࡺࡪ࠳ࡲࡦࡵࡸࡰࡹࡹ᫄ࠧ")
  bstack11ll111lll_opy_ = bstack11l111_opy_ (u"ࠧࡴࡦ࡮࠾ࡦ࠷࠱ࡺ࠼ࡧࡶ࡮ࡼࡥࡳ࠯ࡳࡩࡷ࡬࡯ࡳ࡯ࡶࡧࡦࡴࠧ᫅")
  bstack11111lll11_opy_ = bstack11l111_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡵࡵࡱࡰࡥࡹ࡫࠺࡭ࡱࡦࡥࡱ࠭᫆") #shift
  bstack1ll1l1l1l1_opy_ = bstack11l111_opy_ (u"ࠩࡶࡨࡰࡀࡡࡱࡲ࠰ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠿ࡧࡰࡱ࠯ࡸࡴࡱࡵࡡࡥࠩ᫇") #shift
  bstack11ll111l1_opy_ = bstack11l111_opy_ (u"ࠪࡷࡩࡱ࠺ࡢࡷࡷࡳࡲࡧࡴࡦ࠼ࡦ࡭࠲ࡧࡲࡵ࡫ࡩࡥࡨࡺࡳࠨ᫈")
  bstack1111ll1111_opy_ = bstack11l111_opy_ (u"ࠫࡸࡪ࡫࠻ࡣ࠴࠵ࡾࡀࡧࡦࡶ࠰ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻ࠰ࡶࡪࡹࡵ࡭ࡶࡶ࠱ࡸࡻ࡭࡮ࡣࡵࡽࠬ᫉") #shift
  bstack1llll11111_opy_ = bstack11l111_opy_ (u"ࠬࡹࡤ࡬࠼ࡤ࠵࠶ࡿ࠺ࡨࡧࡷ࠱ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼ࠱ࡷ࡫ࡳࡶ࡮ࡷࡷ᫊ࠬ") #shift
  bstack11l11l1ll1l_opy_ = bstack11l111_opy_ (u"࠭ࡳࡥ࡭࠽ࡴࡪࡸࡣࡺࠩ᫋") #shift
  bstack11lllll1ll1_opy_ = bstack11l111_opy_ (u"ࠧࡴࡦ࡮࠾ࡵ࡫ࡲࡤࡻ࠽ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠧᫌ")
  bstack1ll11l11l_opy_ = bstack11l111_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡵࡵࡱࡰࡥࡹ࡫࠺ࡴࡧࡶࡷ࡮ࡵ࡮࠮ࡵࡷࡥࡹࡻࡳࠨᫍ") #shift
  bstack11l1111ll_opy_ = bstack11l111_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡥ࠻ࡪࡸࡦ࠲ࡳࡡ࡯ࡣࡪࡩࡲ࡫࡮ࡵࠩᫎ")
  bstack11l1l111111_opy_ = bstack11l111_opy_ (u"ࠪࡷࡩࡱ࠺ࡱࡴࡲࡼࡾ࠳ࡳࡦࡶࡸࡴࠬ᫏") #shift
  bstack1111llllll_opy_ = bstack11l111_opy_ (u"ࠫࡸࡪ࡫࠻ࡵࡨࡸࡺࡶࠧ᫐")
  bstack11l1l11l1ll_opy_ = bstack11l111_opy_ (u"ࠬࡹࡤ࡬࠼ࡳࡩࡷࡩࡹ࠻ࡵࡱࡥࡵࡹࡨࡰࡶࠪ᫑") # not bstack11l1l11lll1_opy_ in python
  bstack1l1l11lll_opy_ = bstack11l111_opy_ (u"࠭ࡳࡥ࡭࠽ࡨࡷ࡯ࡶࡦࡴ࠽ࡵࡺ࡯ࡴࠨ᫒") # used in bstack11l1l1l11ll_opy_
  bstack1ll1l1ll11_opy_ = bstack11l111_opy_ (u"ࠧࡴࡦ࡮࠾ࡩࡸࡩࡷࡧࡵ࠾࡬࡫ࡴࠨ᫓") # used in bstack11l1l1l11ll_opy_
  bstack1l1ll1111_opy_ = bstack11l111_opy_ (u"ࠨࡵࡧ࡯࠿࡮࡯ࡰ࡭ࠪ᫔")
  bstack1l111lll1l_opy_ = bstack11l111_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡥ࠻ࡵࡨࡷࡸ࡯࡯࡯࠯ࡱࡥࡲ࡫ࠧ᫕")
  bstack111111lll1_opy_ = bstack11l111_opy_ (u"ࠪࡷࡩࡱ࠺ࡢࡷࡷࡳࡲࡧࡴࡦ࠼ࡶࡩࡸࡹࡩࡰࡰ࠰ࡥࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠧ᫖") #
  bstack1111ll11l1_opy_ = bstack11l111_opy_ (u"ࠫࡸࡪ࡫࠻ࡱ࠴࠵ࡾࡀࡤࡳ࡫ࡹࡩࡷ࠳ࡴࡢ࡭ࡨࡗࡨࡸࡥࡦࡰࡖ࡬ࡴࡺࠧ᫗")
  bstack111lll1ll1_opy_ = bstack11l111_opy_ (u"ࠬࡹࡤ࡬࠼ࡳࡩࡷࡩࡹ࠻ࡣࡸࡸࡴ࠳ࡣࡢࡲࡷࡹࡷ࡫ࠧ᫘")
  bstack1l1111lll1_opy_ = bstack11l111_opy_ (u"࠭ࡳࡥ࡭࠽ࡴࡷ࡫࠭ࡵࡧࡶࡸࠬ᫙")
  bstack11111l1ll1_opy_ = bstack11l111_opy_ (u"ࠧࡴࡦ࡮࠾ࡵࡵࡳࡵ࠯ࡷࡩࡸࡺࠧ᫚")
  bstack1ll1111ll1_opy_ = bstack11l111_opy_ (u"ࠨࡵࡧ࡯࠿ࡪࡲࡪࡸࡨࡶ࠿ࡶࡲࡦ࠯࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡦࡺࡩࡰࡰࠪ᫛") #shift
  bstack111l11ll1l_opy_ = bstack11l111_opy_ (u"ࠩࡶࡨࡰࡀࡤࡳ࡫ࡹࡩࡷࡀࡰࡰࡵࡷ࠱࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࢀࡡࡵ࡫ࡲࡲࠬ᫜") #shift
  bstack11l11lllll1_opy_ = bstack11l111_opy_ (u"ࠪࡷࡩࡱ࠺ࡢࡷࡷࡳ࠲ࡩࡡࡱࡶࡸࡶࡪ࠭᫝")
  bstack11l1l111ll1_opy_ = bstack11l111_opy_ (u"ࠫࡸࡪ࡫࠻ࡣࡸࡸࡴࡳࡡࡵࡧ࠽࡭ࡩࡲࡥ࠮ࡶ࡬ࡱࡪࡵࡵࡵࠩ᫞")
  bstack1l1l1111111_opy_ = bstack11l111_opy_ (u"ࠬࡹࡤ࡬࠼ࡦࡰ࡮ࡀࡳࡵࡣࡵࡸࠬ᫟")
  bstack11l1l11l11l_opy_ = bstack11l111_opy_ (u"࠭ࡳࡥ࡭࠽ࡧࡱ࡯࠺ࡥࡱࡺࡲࡱࡵࡡࡥࠩ᫠")
  bstack11l11llllll_opy_ = bstack11l111_opy_ (u"ࠧࡴࡦ࡮࠾ࡨࡲࡩ࠻ࡥ࡫ࡩࡨࡱ࠭ࡶࡲࡧࡥࡹ࡫ࠧ᫡")
  bstack1l1l11l111l_opy_ = bstack11l111_opy_ (u"ࠨࡵࡧ࡯࠿ࡩ࡬ࡪ࠼ࡲࡲ࠲ࡨ࡯ࡰࡶࡶࡸࡷࡧࡰࠨ᫢")
  bstack1l11llll11l_opy_ = bstack11l111_opy_ (u"ࠩࡶࡨࡰࡀࡣ࡭࡫࠽ࡳࡳ࠳ࡣࡰࡰࡱࡩࡨࡺࠧ᫣")
  bstack1l1l111lll1_opy_ = bstack11l111_opy_ (u"ࠪࡷࡩࡱ࠺ࡤ࡮࡬࠾ࡴࡴ࠭ࡴࡶࡲࡴࠬ᫤")
  bstack1l1l111llll_opy_ = bstack11l111_opy_ (u"ࠫࡸࡪ࡫࠻ࡵࡷࡥࡷࡺࡂࡪࡰࡖࡩࡸࡹࡩࡰࡰࠪ᫥")
  bstack1l1l111111l_opy_ = bstack11l111_opy_ (u"ࠬࡹࡤ࡬࠼ࡦࡳࡳࡴࡥࡤࡶࡅ࡭ࡳ࡙ࡥࡴࡵ࡬ࡳࡳ࠭᫦")
  bstack11l1l111l1l_opy_ = bstack11l111_opy_ (u"࠭ࡳࡥ࡭࠽ࡨࡷ࡯ࡶࡦࡴࡌࡲ࡮ࡺࠧ᫧")
  bstack11l1l11l111_opy_ = bstack11l111_opy_ (u"ࠧࡴࡦ࡮࠾࡫࡯࡮ࡥࡐࡨࡥࡷ࡫ࡳࡵࡊࡸࡦࠬ᫨")
  bstack1lllll111l1_opy_ = bstack11l111_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡍࡳ࡯ࡴࠨ᫩")
  bstack1lllll111ll_opy_ = bstack11l111_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࡘࡺࡡࡳࡶࠪ᫪")
  bstack1l111l1ll1l_opy_ = bstack11l111_opy_ (u"ࠪࡷࡩࡱ࠺ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡃࡰࡰࡩ࡭࡬࠭᫫")
  bstack11l11llll11_opy_ = bstack11l111_opy_ (u"ࠫࡸࡪ࡫࠻ࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࡄࡱࡱࡪ࡮࡭ࠧ᫬")
  bstack1l1ll111ll1_opy_ = bstack11l111_opy_ (u"ࠬࡹࡤ࡬࠼ࡤ࡭ࡘ࡫࡬ࡧࡊࡨࡥࡱ࡙ࡴࡦࡲࠪ᫭")
  bstack1l1ll11lll1_opy_ = bstack11l111_opy_ (u"࠭ࡳࡥ࡭࠽ࡥ࡮࡙ࡥ࡭ࡨࡋࡩࡦࡲࡇࡦࡶࡕࡩࡸࡻ࡬ࡵࠩ᫮")
  bstack1l11l111l11_opy_ = bstack11l111_opy_ (u"ࠧࡴࡦ࡮࠾ࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡉࡻ࡫࡮ࡵࠩ᫯")
  bstack1l11l11111l_opy_ = bstack11l111_opy_ (u"ࠨࡵࡧ࡯࠿ࡺࡥࡴࡶࡖࡩࡸࡹࡩࡰࡰࡈࡺࡪࡴࡴࠨ᫰")
  bstack1l111llll1l_opy_ = bstack11l111_opy_ (u"ࠩࡶࡨࡰࡀࡣ࡭࡫࠽ࡰࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࡅࡷࡧࡱࡸࠬ᫱")
  bstack11l1l11ll11_opy_ = bstack11l111_opy_ (u"ࠪࡷࡩࡱ࠺ࡤ࡮࡬࠾ࡪࡴࡱࡶࡧࡸࡩ࡙࡫ࡳࡵࡇࡹࡩࡳࡺࠧ᫲")
  bstack1llll11ll1l_opy_ = bstack11l111_opy_ (u"ࠫࡸࡪ࡫࠻ࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࡓࡵࡱࡳࠫ᫳")
  bstack1l1l1l1ll11_opy_ = bstack11l111_opy_ (u"ࠬࡹࡤ࡬࠼ࡲࡲࡘࡺ࡯ࡱࠩ᫴")
class STAGE(Enum):
  bstack1lll111l1l_opy_ = bstack11l111_opy_ (u"࠭ࡳࡵࡣࡵࡸࠬ᫵")
  END = bstack11l111_opy_ (u"ࠧࡦࡰࡧࠫ᫶")
  bstack1l11lll11_opy_ = bstack11l111_opy_ (u"ࠨࡵ࡬ࡲ࡬ࡲࡥࠨ᫷")
bstack11l1111l1l_opy_ = {
  bstack11l111_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࠩ᫸"): bstack11l111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ᫹"),
  bstack11l111_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗ࠱ࡇࡊࡄࠨ᫺"): bstack11l111_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸ࠲ࡩࡵࡤࡷࡰࡦࡪࡸࠧ᫻")
}
PLAYWRIGHT_HUB_URL = bstack11l111_opy_ (u"ࠨࡷࡴࡵ࠽࠳࠴ࡩࡤࡱ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡁࡦࡥࡵࡹ࠽ࠣ᫼")
bstack1l111l1l1ll_opy_ = 98
bstack1l1111l1111_opy_ = 100
bstack111ll111_opy_ = {
  bstack11l111_opy_ (u"ࠧࡳࡧࡵࡹࡳ࠭᫽"): bstack11l111_opy_ (u"ࠨ࠯࠰ࡶࡪࡸࡵ࡯ࡵࠪ᫾"),
  bstack11l111_opy_ (u"ࠩࡧࡩࡱࡧࡹࠨ᫿"): bstack11l111_opy_ (u"ࠪ࠱࠲ࡸࡥࡳࡷࡱࡷ࠲ࡪࡥ࡭ࡣࡼࠫᬀ"),
  bstack11l111_opy_ (u"ࠫࡷ࡫ࡲࡶࡰ࠰ࡨࡪࡲࡡࡺࠩᬁ"): 0
}
bstack11ll1ll1l1l_opy_ = bstack11l111_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡣࡰ࡮࡯ࡩࡨࡺ࡯ࡳ࠯ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠧᬂ")
bstack11l11ll1ll1_opy_ = bstack11l111_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࡶࡲ࡯ࡳࡦࡪ࠭ࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠥᬃ")
bstack11l111l111_opy_ = bstack11l111_opy_ (u"ࠢࡕࡇࡖࡘࠥࡘࡅࡑࡑࡕࡘࡎࡔࡇࠡࡃࡑࡈࠥࡇࡎࡂࡎ࡜ࡘࡎࡉࡓࠣᬄ")