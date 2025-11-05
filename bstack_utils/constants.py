# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import os
import re
from enum import Enum
bstack1ll11l1l11_opy_ = {
  bstack11ll1ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ២"): bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫ࡲࠨ៣"),
  bstack11ll1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ៤"): bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡱࡥࡺࠩ៥"),
  bstack11ll1ll_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪ៦"): bstack11ll1ll_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ៧"),
  bstack11ll1ll_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩ៨"): bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡸࡷࡪࡥࡷ࠴ࡥࠪ៩"),
  bstack11ll1ll_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩ៪"): bstack11ll1ll_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹ࠭៫"),
  bstack11ll1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ៬"): bstack11ll1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩ࠭៭"),
  bstack11ll1ll_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭៮"): bstack11ll1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ៯"),
  bstack11ll1ll_opy_ (u"ࠪࡨࡪࡨࡵࡨࠩ៰"): bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡨࡪࡨࡵࡨࠩ៱"),
  bstack11ll1ll_opy_ (u"ࠬࡩ࡯࡯ࡵࡲࡰࡪࡒ࡯ࡨࡵࠪ៲"): bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡯ࡵࡲࡰࡪ࠭៳"),
  bstack11ll1ll_opy_ (u"ࠧ࡯ࡧࡷࡻࡴࡸ࡫ࡍࡱࡪࡷࠬ៴"): bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡯ࡧࡷࡻࡴࡸ࡫ࡍࡱࡪࡷࠬ៵"),
  bstack11ll1ll_opy_ (u"ࠩࡤࡴࡵ࡯ࡵ࡮ࡎࡲ࡫ࡸ࠭៶"): bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡴࡵ࡯ࡵ࡮ࡎࡲ࡫ࡸ࠭៷"),
  bstack11ll1ll_opy_ (u"ࠫࡻ࡯ࡤࡦࡱࠪ៸"): bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡻ࡯ࡤࡦࡱࠪ៹"),
  bstack11ll1ll_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡍࡱࡪࡷࠬ៺"): bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡍࡱࡪࡷࠬ៻"),
  bstack11ll1ll_opy_ (u"ࠨࡶࡨࡰࡪࡳࡥࡵࡴࡼࡐࡴ࡭ࡳࠨ៼"): bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡶࡨࡰࡪࡳࡥࡵࡴࡼࡐࡴ࡭ࡳࠨ៽"),
  bstack11ll1ll_opy_ (u"ࠪ࡫ࡪࡵࡌࡰࡥࡤࡸ࡮ࡵ࡮ࠨ៾"): bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱࡫ࡪࡵࡌࡰࡥࡤࡸ࡮ࡵ࡮ࠨ៿"),
  bstack11ll1ll_opy_ (u"ࠬࡺࡩ࡮ࡧࡽࡳࡳ࡫ࠧ᠀"): bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡺࡩ࡮ࡧࡽࡳࡳ࡫ࠧ᠁"),
  bstack11ll1ll_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩ᠂"): bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠪ᠃"),
  bstack11ll1ll_opy_ (u"ࠩࡰࡥࡸࡱࡃࡰ࡯ࡰࡥࡳࡪࡳࠨ᠄"): bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡰࡥࡸࡱࡃࡰ࡯ࡰࡥࡳࡪࡳࠨ᠅"),
  bstack11ll1ll_opy_ (u"ࠫ࡮ࡪ࡬ࡦࡖ࡬ࡱࡪࡵࡵࡵࠩ᠆"): bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡮ࡪ࡬ࡦࡖ࡬ࡱࡪࡵࡵࡵࠩ᠇"),
  bstack11ll1ll_opy_ (u"࠭࡭ࡢࡵ࡮ࡆࡦࡹࡩࡤࡃࡸࡸ࡭࠭᠈"): bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡭ࡢࡵ࡮ࡆࡦࡹࡩࡤࡃࡸࡸ࡭࠭᠉"),
  bstack11ll1ll_opy_ (u"ࠨࡵࡨࡲࡩࡑࡥࡺࡵࠪ᠊"): bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡵࡨࡲࡩࡑࡥࡺࡵࠪ᠋"),
  bstack11ll1ll_opy_ (u"ࠪࡥࡺࡺ࡯ࡘࡣ࡬ࡸࠬ᠌"): bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡺࡺ࡯ࡘࡣ࡬ࡸࠬ᠍"),
  bstack11ll1ll_opy_ (u"ࠬ࡮࡯ࡴࡶࡶࠫ᠎"): bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡮࡯ࡴࡶࡶࠫ᠏"),
  bstack11ll1ll_opy_ (u"ࠧࡣࡨࡦࡥࡨ࡮ࡥࠨ᠐"): bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡨࡦࡥࡨ࡮ࡥࠨ᠑"),
  bstack11ll1ll_opy_ (u"ࠩࡺࡷࡑࡵࡣࡢ࡮ࡖࡹࡵࡶ࡯ࡳࡶࠪ᠒"): bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡺࡷࡑࡵࡣࡢ࡮ࡖࡹࡵࡶ࡯ࡳࡶࠪ᠓"),
  bstack11ll1ll_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡈࡵࡲࡴࡔࡨࡷࡹࡸࡩࡤࡶ࡬ࡳࡳࡹࠧ᠔"): bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡩ࡯ࡳࡢࡤ࡯ࡩࡈࡵࡲࡴࡔࡨࡷࡹࡸࡩࡤࡶ࡬ࡳࡳࡹࠧ᠕"),
  bstack11ll1ll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪ᠖"): bstack11ll1ll_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ᠗"),
  bstack11ll1ll_opy_ (u"ࠨࡴࡨࡥࡱࡓ࡯ࡣ࡫࡯ࡩࠬ᠘"): bstack11ll1ll_opy_ (u"ࠩࡵࡩࡦࡲ࡟࡮ࡱࡥ࡭ࡱ࡫ࠧ᠙"),
  bstack11ll1ll_opy_ (u"ࠪࡥࡵࡶࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ᠚"): bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡵࡶࡩࡶ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫ᠛"),
  bstack11ll1ll_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡓ࡫ࡴࡸࡱࡵ࡯ࠬ᠜"): bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩࡵࡴࡶࡲࡱࡓ࡫ࡴࡸࡱࡵ࡯ࠬ᠝"),
  bstack11ll1ll_opy_ (u"ࠧ࡯ࡧࡷࡻࡴࡸ࡫ࡑࡴࡲࡪ࡮ࡲࡥࠨ᠞"): bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡯ࡧࡷࡻࡴࡸ࡫ࡑࡴࡲࡪ࡮ࡲࡥࠨ᠟"),
  bstack11ll1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡰࡵࡋࡱࡷࡪࡩࡵࡳࡧࡆࡩࡷࡺࡳࠨᠠ"): bstack11ll1ll_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡖࡷࡱࡉࡥࡳࡶࡶࠫᠡ"),
  bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ᠢ"): bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ᠣ"),
  bstack11ll1ll_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ᠤ"): bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡳࡰࡷࡵࡧࡪ࠭ᠥ"),
  bstack11ll1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᠦ"): bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᠧ"),
  bstack11ll1ll_opy_ (u"ࠪ࡬ࡴࡹࡴࡏࡣࡰࡩࠬᠨ"): bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱࡬ࡴࡹࡴࡏࡣࡰࡩࠬᠩ"),
  bstack11ll1ll_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡘ࡯࡭ࠨᠪ"): bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡫࡮ࡢࡤ࡯ࡩࡘ࡯࡭ࠨᠫ"),
  bstack11ll1ll_opy_ (u"ࠧࡴ࡫ࡰࡓࡵࡺࡩࡰࡰࡶࠫᠬ"): bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡴ࡫ࡰࡓࡵࡺࡩࡰࡰࡶࠫᠭ"),
  bstack11ll1ll_opy_ (u"ࠩࡸࡴࡱࡵࡡࡥࡏࡨࡨ࡮ࡧࠧᠮ"): bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡸࡴࡱࡵࡡࡥࡏࡨࡨ࡮ࡧࠧᠯ"),
  bstack11ll1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧᠰ"): bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧᠱ"),
  bstack11ll1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨᠲ"): bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨᠳ")
}
bstack11l1l11l111_opy_ = [
  bstack11ll1ll_opy_ (u"ࠨࡱࡶࠫᠴ"),
  bstack11ll1ll_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬᠵ"),
  bstack11ll1ll_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬᠶ"),
  bstack11ll1ll_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩᠷ"),
  bstack11ll1ll_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩᠸ"),
  bstack11ll1ll_opy_ (u"࠭ࡲࡦࡣ࡯ࡑࡴࡨࡩ࡭ࡧࠪᠹ"),
  bstack11ll1ll_opy_ (u"ࠧࡢࡲࡳ࡭ࡺࡳࡖࡦࡴࡶ࡭ࡴࡴࠧᠺ"),
]
bstack1l11lll1l1_opy_ = {
  bstack11ll1ll_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪᠻ"): [bstack11ll1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡗࡖࡉࡗࡔࡁࡎࡇࠪᠼ"), bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡘࡗࡊࡘ࡟ࡏࡃࡐࡉࠬᠽ")],
  bstack11ll1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧᠾ"): bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆࡉࡃࡆࡕࡖࡣࡐࡋ࡙ࠨᠿ"),
  bstack11ll1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩᡀ"): bstack11ll1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡔࡁࡎࡇࠪᡁ"),
  bstack11ll1ll_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ᡂ"): bstack11ll1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡕࡓࡏࡋࡃࡕࡡࡑࡅࡒࡋࠧᡃ"),
  bstack11ll1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬᡄ"): bstack11ll1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ᡅ"),
  bstack11ll1ll_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬᡆ"): bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡁࡓࡃࡏࡐࡊࡒࡓࡠࡒࡈࡖࡤࡖࡌࡂࡖࡉࡓࡗࡓࠧᡇ"),
  bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫᡈ"): bstack11ll1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑ࠭ᡉ"),
  bstack11ll1ll_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࡕࡧࡶࡸࡸ࠭ᡊ"): bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࡠࡖࡈࡗ࡙࡙ࠧᡋ"),
  bstack11ll1ll_opy_ (u"ࠫࡦࡶࡰࠨᡌ"): [bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆࡖࡐࡠࡋࡇࠫᡍ"), bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡐࡑࠩᡎ")],
  bstack11ll1ll_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩᡏ"): bstack11ll1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡔࡆࡎࡣࡑࡕࡇࡍࡇ࡙ࡉࡑ࠭ᡐ"),
  bstack11ll1ll_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᡑ"): bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ᡒ"),
  bstack11ll1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨᡓ"): [bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡒࡆࡘࡋࡒࡗࡃࡅࡍࡑࡏࡔ࡚ࠩᡔ"), bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡖࡊࡖࡏࡓࡖࡌࡒࡌ࠭ᡕ")],
  bstack11ll1ll_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫᡖ"): bstack11ll1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡗࡕࡆࡔ࡙ࡃࡂࡎࡈࠫᡗ"),
  bstack11ll1ll_opy_ (u"ࠩࡶࡱࡦࡸࡴࡔࡧ࡯ࡩࡨࡺࡩࡰࡰࡉࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࡧࡶࡉࡓ࡜ࠧᡘ"): bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡒࡖࡈࡎࡅࡔࡖࡕࡅ࡙ࡏࡏࡏࡡࡖࡑࡆࡘࡔࡠࡕࡈࡐࡊࡉࡔࡊࡑࡑࡣࡋࡋࡁࡕࡗࡕࡉࡤࡈࡒࡂࡐࡆࡌࡊ࡙ࠧᡙ")
}
bstack1111l1ll1l_opy_ = {
  bstack11ll1ll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ᡚ"): [bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡳࡡࡱࡥࡲ࡫ࠧᡛ"), bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡻࡳࡦࡴࡑࡥࡲ࡫ࠧᡜ")],
  bstack11ll1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪᡝ"): [bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹ࡟࡬ࡧࡼࠫᡞ"), bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫᡟ")],
  bstack11ll1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ᡠ"): bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ᡡ"),
  bstack11ll1ll_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪᡢ"): bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪᡣ"),
  bstack11ll1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᡤ"): bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᡥ"),
  bstack11ll1ll_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩᡦ"): [bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡳࡴࡵ࠭ᡧ"), bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᡨ")],
  bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩᡩ"): bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࠫᡪ"),
  bstack11ll1ll_opy_ (u"ࠧࡳࡧࡵࡹࡳ࡚ࡥࡴࡶࡶࠫᡫ"): bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡳࡧࡵࡹࡳ࡚ࡥࡴࡶࡶࠫᡬ"),
  bstack11ll1ll_opy_ (u"ࠩࡤࡴࡵ࠭ᡭ"): bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡴࡵ࠭ᡮ"),
  bstack11ll1ll_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭ᡯ"): bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡧࡍࡧࡹࡩࡱ࠭ᡰ"),
  bstack11ll1ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᡱ"): bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᡲ"),
  bstack11ll1ll_opy_ (u"ࠣࡵࡰࡥࡷࡺࡓࡦ࡮ࡨࡧࡹ࡯࡯࡯ࡈࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࡦࡵࡆࡐࡎࠨᡳ"): bstack11ll1ll_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠳ࡹ࡭ࡢࡴࡷࡗࡪࡲࡥࡤࡶ࡬ࡳࡳࡌࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࡪࡹࠢᡴ"),
}
bstack111l1l111_opy_ = {
  bstack11ll1ll_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᡵ"): bstack11ll1ll_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᡶ"),
  bstack11ll1ll_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡖࡦࡴࡶ࡭ࡴࡴࠧᡷ"): [bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᡸ"), bstack11ll1ll_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠪ᡹")],
  bstack11ll1ll_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭᡺"): bstack11ll1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ᡻"),
  bstack11ll1ll_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧ᡼"): bstack11ll1ll_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫ᡽"),
  bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ᡾"): [bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧ᡿"), bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡰࡤࡱࡪ࠭ᢀ")],
  bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᢁ"): bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫᢂ"),
  bstack11ll1ll_opy_ (u"ࠪࡶࡪࡧ࡬ࡎࡱࡥ࡭ࡱ࡫ࠧᢃ"): bstack11ll1ll_opy_ (u"ࠫࡷ࡫ࡡ࡭ࡡࡰࡳࡧ࡯࡬ࡦࠩᢄ"),
  bstack11ll1ll_opy_ (u"ࠬࡧࡰࡱ࡫ࡸࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬᢅ"): [bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡰࡱ࡫ࡸࡱࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᢆ"), bstack11ll1ll_opy_ (u"ࠧࡢࡲࡳ࡭ࡺࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᢇ")],
  bstack11ll1ll_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡊࡰࡶࡩࡨࡻࡲࡦࡅࡨࡶࡹࡹࠧᢈ"): [bstack11ll1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡰࡵࡕࡶࡰࡈ࡫ࡲࡵࡵࠪᢉ"), bstack11ll1ll_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡖࡷࡱࡉࡥࡳࡶࠪᢊ")]
}
bstack1l11111ll1_opy_ = [
  bstack11ll1ll_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡍࡳࡹࡥࡤࡷࡵࡩࡈ࡫ࡲࡵࡵࠪᢋ"),
  bstack11ll1ll_opy_ (u"ࠬࡶࡡࡨࡧࡏࡳࡦࡪࡓࡵࡴࡤࡸࡪ࡭ࡹࠨᢌ"),
  bstack11ll1ll_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬᢍ"),
  bstack11ll1ll_opy_ (u"ࠧࡴࡧࡷ࡛࡮ࡴࡤࡰࡹࡕࡩࡨࡺࠧᢎ"),
  bstack11ll1ll_opy_ (u"ࠨࡶ࡬ࡱࡪࡵࡵࡵࡵࠪᢏ"),
  bstack11ll1ll_opy_ (u"ࠩࡶࡸࡷ࡯ࡣࡵࡈ࡬ࡰࡪࡏ࡮ࡵࡧࡵࡥࡨࡺࡡࡣ࡫࡯࡭ࡹࡿࠧᢐ"),
  bstack11ll1ll_opy_ (u"ࠪࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡖࡲࡰ࡯ࡳࡸࡇ࡫ࡨࡢࡸ࡬ࡳࡷ࠭ᢑ"),
  bstack11ll1ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᢒ"),
  bstack11ll1ll_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡩ࡭ࡷ࡫ࡦࡰࡺࡒࡴࡹ࡯࡯࡯ࡵࠪᢓ"),
  bstack11ll1ll_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧᢔ"),
  bstack11ll1ll_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᢕ"),
  bstack11ll1ll_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩ࠯ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᢖ"),
]
bstack11ll1llll1_opy_ = [
  bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ᢗ"),
  bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧᢘ"),
  bstack11ll1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪᢙ"),
  bstack11ll1ll_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬᢚ"),
  bstack11ll1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩᢛ"),
  bstack11ll1ll_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩᢜ"),
  bstack11ll1ll_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫᢝ"),
  bstack11ll1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ᢞ"),
  bstack11ll1ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ᢟ"),
  bstack11ll1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠩᢠ"),
  bstack11ll1ll_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩᢡ"),
  bstack11ll1ll_opy_ (u"࠭ࡴࡦࡵࡷࡖࡪࡶ࡯ࡳࡶ࡬ࡲ࡬࠭ᢢ"),
  bstack11ll1ll_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠩᢣ"),
  bstack11ll1ll_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡕࡣࡪࠫᢤ"),
  bstack11ll1ll_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᢥ"),
  bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᢦ"),
  bstack11ll1ll_opy_ (u"ࠫࡷ࡫ࡲࡶࡰࡗࡩࡸࡺࡳࠨᢧ"),
  bstack11ll1ll_opy_ (u"ࠬࡉࡕࡔࡖࡒࡑࡤ࡚ࡁࡈࡡ࠴ࠫᢨ"),
  bstack11ll1ll_opy_ (u"࠭ࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢ࠶ᢩࠬ"),
  bstack11ll1ll_opy_ (u"ࠧࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣ࠸࠭ᢪ"),
  bstack11ll1ll_opy_ (u"ࠨࡅࡘࡗ࡙ࡕࡍࡠࡖࡄࡋࡤ࠺ࠧ᢫"),
  bstack11ll1ll_opy_ (u"ࠩࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࠵ࠨ᢬"),
  bstack11ll1ll_opy_ (u"ࠪࡇ࡚࡙ࡔࡐࡏࡢࡘࡆࡍ࡟࠷ࠩ᢭"),
  bstack11ll1ll_opy_ (u"ࠫࡈ࡛ࡓࡕࡑࡐࡣ࡙ࡇࡇࡠ࠹ࠪ᢮"),
  bstack11ll1ll_opy_ (u"ࠬࡉࡕࡔࡖࡒࡑࡤ࡚ࡁࡈࡡ࠻ࠫ᢯"),
  bstack11ll1ll_opy_ (u"࠭ࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢ࠽ࠬᢰ"),
  bstack11ll1ll_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ᢱ"),
  bstack11ll1ll_opy_ (u"ࠨࡲࡨࡶࡨࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᢲ"),
  bstack11ll1ll_opy_ (u"ࠩࡳࡩࡷࡩࡹࡄࡣࡳࡸࡺࡸࡥࡎࡱࡧࡩࠬᢳ"),
  bstack11ll1ll_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡺࡺ࡯ࡄࡣࡳࡸࡺࡸࡥࡍࡱࡪࡷࠬᢴ"),
  bstack11ll1ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨᢵ"),
  bstack11ll1ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᢶ"),
  bstack11ll1ll_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪᢷ"),
  bstack11ll1ll_opy_ (u"ࠧࡩࡷࡥࡖࡪ࡭ࡩࡰࡰࠪᢸ")
]
bstack11l1l111111_opy_ = [
  bstack11ll1ll_opy_ (u"ࠨࡷࡳࡰࡴࡧࡤࡎࡧࡧ࡭ࡦ࠭ᢹ"),
  bstack11ll1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᢺ"),
  bstack11ll1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᢻ"),
  bstack11ll1ll_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩᢼ"),
  bstack11ll1ll_opy_ (u"ࠬࡺࡥࡴࡶࡓࡶ࡮ࡵࡲࡪࡶࡼࠫᢽ"),
  bstack11ll1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩᢾ"),
  bstack11ll1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩ࡚ࡡࡨࠩᢿ"),
  bstack11ll1ll_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ᣀ"),
  bstack11ll1ll_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫᣁ"),
  bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨᣂ"),
  bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᣃ"),
  bstack11ll1ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫᣄ"),
  bstack11ll1ll_opy_ (u"࠭࡯ࡴࠩᣅ"),
  bstack11ll1ll_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪᣆ"),
  bstack11ll1ll_opy_ (u"ࠨࡪࡲࡷࡹࡹࠧᣇ"),
  bstack11ll1ll_opy_ (u"ࠩࡤࡹࡹࡵࡗࡢ࡫ࡷࠫᣈ"),
  bstack11ll1ll_opy_ (u"ࠪࡶࡪ࡭ࡩࡰࡰࠪᣉ"),
  bstack11ll1ll_opy_ (u"ࠫࡹ࡯࡭ࡦࡼࡲࡲࡪ࠭ᣊ"),
  bstack11ll1ll_opy_ (u"ࠬࡳࡡࡤࡪ࡬ࡲࡪ࠭ᣋ"),
  bstack11ll1ll_opy_ (u"࠭ࡲࡦࡵࡲࡰࡺࡺࡩࡰࡰࠪᣌ"),
  bstack11ll1ll_opy_ (u"ࠧࡪࡦ࡯ࡩ࡙࡯࡭ࡦࡱࡸࡸࠬᣍ"),
  bstack11ll1ll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡐࡴ࡬ࡩࡳࡺࡡࡵ࡫ࡲࡲࠬᣎ"),
  bstack11ll1ll_opy_ (u"ࠩࡹ࡭ࡩ࡫࡯ࠨᣏ"),
  bstack11ll1ll_opy_ (u"ࠪࡲࡴࡖࡡࡨࡧࡏࡳࡦࡪࡔࡪ࡯ࡨࡳࡺࡺࠧᣐ"),
  bstack11ll1ll_opy_ (u"ࠫࡧ࡬ࡣࡢࡥ࡫ࡩࠬᣑ"),
  bstack11ll1ll_opy_ (u"ࠬࡪࡥࡣࡷࡪࠫᣒ"),
  bstack11ll1ll_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲ࡙ࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪᣓ"),
  bstack11ll1ll_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡓࡦࡰࡧࡏࡪࡿࡳࠨᣔ"),
  bstack11ll1ll_opy_ (u"ࠨࡴࡨࡥࡱࡓ࡯ࡣ࡫࡯ࡩࠬᣕ"),
  bstack11ll1ll_opy_ (u"ࠩࡱࡳࡕ࡯ࡰࡦ࡮࡬ࡲࡪ࠭ᣖ"),
  bstack11ll1ll_opy_ (u"ࠪࡧ࡭࡫ࡣ࡬ࡗࡕࡐࠬᣗ"),
  bstack11ll1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᣘ"),
  bstack11ll1ll_opy_ (u"ࠬࡧࡣࡤࡧࡳࡸࡈࡵ࡯࡬࡫ࡨࡷࠬᣙ"),
  bstack11ll1ll_opy_ (u"࠭ࡣࡢࡲࡷࡹࡷ࡫ࡃࡳࡣࡶ࡬ࠬᣚ"),
  bstack11ll1ll_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫᣛ"),
  bstack11ll1ll_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᣜ"),
  bstack11ll1ll_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᣝ"),
  bstack11ll1ll_opy_ (u"ࠪࡲࡴࡈ࡬ࡢࡰ࡮ࡔࡴࡲ࡬ࡪࡰࡪࠫᣞ"),
  bstack11ll1ll_opy_ (u"ࠫࡲࡧࡳ࡬ࡕࡨࡲࡩࡑࡥࡺࡵࠪᣟ"),
  bstack11ll1ll_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡑࡵࡧࡴࠩᣠ"),
  bstack11ll1ll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡏࡤࠨᣡ"),
  bstack11ll1ll_opy_ (u"ࠧࡥࡧࡧ࡭ࡨࡧࡴࡦࡦࡇࡩࡻ࡯ࡣࡦࠩᣢ"),
  bstack11ll1ll_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡑࡣࡵࡥࡲࡹࠧᣣ"),
  bstack11ll1ll_opy_ (u"ࠩࡳ࡬ࡴࡴࡥࡏࡷࡰࡦࡪࡸࠧᣤ"),
  bstack11ll1ll_opy_ (u"ࠪࡲࡪࡺࡷࡰࡴ࡮ࡐࡴ࡭ࡳࠨᣥ"),
  bstack11ll1ll_opy_ (u"ࠫࡳ࡫ࡴࡸࡱࡵ࡯ࡑࡵࡧࡴࡑࡳࡸ࡮ࡵ࡮ࡴࠩᣦ"),
  bstack11ll1ll_opy_ (u"ࠬࡩ࡯࡯ࡵࡲࡰࡪࡒ࡯ࡨࡵࠪᣧ"),
  bstack11ll1ll_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ᣨ"),
  bstack11ll1ll_opy_ (u"ࠧࡢࡲࡳ࡭ࡺࡳࡌࡰࡩࡶࠫᣩ"),
  bstack11ll1ll_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡃ࡫ࡲࡱࡪࡺࡲࡪࡥࠪᣪ"),
  bstack11ll1ll_opy_ (u"ࠩࡹ࡭ࡩ࡫࡯ࡗ࠴ࠪᣫ"),
  bstack11ll1ll_opy_ (u"ࠪࡱ࡮ࡪࡓࡦࡵࡶ࡭ࡴࡴࡉ࡯ࡵࡷࡥࡱࡲࡁࡱࡲࡶࠫᣬ"),
  bstack11ll1ll_opy_ (u"ࠫࡪࡹࡰࡳࡧࡶࡷࡴ࡙ࡥࡳࡸࡨࡶࠬᣭ"),
  bstack11ll1ll_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡌࡰࡩࡶࠫᣮ"),
  bstack11ll1ll_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡄࡦࡳࠫᣯ"),
  bstack11ll1ll_opy_ (u"ࠧࡵࡧ࡯ࡩࡲ࡫ࡴࡳࡻࡏࡳ࡬ࡹࠧᣰ"),
  bstack11ll1ll_opy_ (u"ࠨࡵࡼࡲࡨ࡚ࡩ࡮ࡧ࡚࡭ࡹ࡮ࡎࡕࡒࠪᣱ"),
  bstack11ll1ll_opy_ (u"ࠩࡪࡩࡴࡒ࡯ࡤࡣࡷ࡭ࡴࡴࠧᣲ"),
  bstack11ll1ll_opy_ (u"ࠪ࡫ࡵࡹࡌࡰࡥࡤࡸ࡮ࡵ࡮ࠨᣳ"),
  bstack11ll1ll_opy_ (u"ࠫࡳ࡫ࡴࡸࡱࡵ࡯ࡕࡸ࡯ࡧ࡫࡯ࡩࠬᣴ"),
  bstack11ll1ll_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡓ࡫ࡴࡸࡱࡵ࡯ࠬᣵ"),
  bstack11ll1ll_opy_ (u"࠭ࡦࡰࡴࡦࡩࡈ࡮ࡡ࡯ࡩࡨࡎࡦࡸࠧ᣶"),
  bstack11ll1ll_opy_ (u"ࠧࡹ࡯ࡶࡎࡦࡸࠧ᣷"),
  bstack11ll1ll_opy_ (u"ࠨࡺࡰࡼࡏࡧࡲࠨ᣸"),
  bstack11ll1ll_opy_ (u"ࠩࡰࡥࡸࡱࡃࡰ࡯ࡰࡥࡳࡪࡳࠨ᣹"),
  bstack11ll1ll_opy_ (u"ࠪࡱࡦࡹ࡫ࡃࡣࡶ࡭ࡨࡇࡵࡵࡪࠪ᣺"),
  bstack11ll1ll_opy_ (u"ࠫࡼࡹࡌࡰࡥࡤࡰࡘࡻࡰࡱࡱࡵࡸࠬ᣻"),
  bstack11ll1ll_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡉ࡯ࡳࡵࡕࡩࡸࡺࡲࡪࡥࡷ࡭ࡴࡴࡳࠨ᣼"),
  bstack11ll1ll_opy_ (u"࠭ࡡࡱࡲ࡙ࡩࡷࡹࡩࡰࡰࠪ᣽"),
  bstack11ll1ll_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡉ࡯ࡵࡨࡧࡺࡸࡥࡄࡧࡵࡸࡸ࠭᣾"),
  bstack11ll1ll_opy_ (u"ࠨࡴࡨࡷ࡮࡭࡮ࡂࡲࡳࠫ᣿"),
  bstack11ll1ll_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡲ࡮ࡳࡡࡵ࡫ࡲࡲࡸ࠭ᤀ"),
  bstack11ll1ll_opy_ (u"ࠪࡧࡦࡴࡡࡳࡻࠪᤁ"),
  bstack11ll1ll_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬᤂ"),
  bstack11ll1ll_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬᤃ"),
  bstack11ll1ll_opy_ (u"࠭ࡩࡦࠩᤄ"),
  bstack11ll1ll_opy_ (u"ࠧࡦࡦࡪࡩࠬᤅ"),
  bstack11ll1ll_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨᤆ"),
  bstack11ll1ll_opy_ (u"ࠩࡴࡹࡪࡻࡥࠨᤇ"),
  bstack11ll1ll_opy_ (u"ࠪ࡭ࡳࡺࡥࡳࡰࡤࡰࠬᤈ"),
  bstack11ll1ll_opy_ (u"ࠫࡦࡶࡰࡔࡶࡲࡶࡪࡉ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠬᤉ"),
  bstack11ll1ll_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡈࡧ࡭ࡦࡴࡤࡍࡲࡧࡧࡦࡋࡱ࡮ࡪࡩࡴࡪࡱࡱࠫᤊ"),
  bstack11ll1ll_opy_ (u"࠭࡮ࡦࡶࡺࡳࡷࡱࡌࡰࡩࡶࡉࡽࡩ࡬ࡶࡦࡨࡌࡴࡹࡴࡴࠩᤋ"),
  bstack11ll1ll_opy_ (u"ࠧ࡯ࡧࡷࡻࡴࡸ࡫ࡍࡱࡪࡷࡎࡴࡣ࡭ࡷࡧࡩࡍࡵࡳࡵࡵࠪᤌ"),
  bstack11ll1ll_opy_ (u"ࠨࡷࡳࡨࡦࡺࡥࡂࡲࡳࡗࡪࡺࡴࡪࡰࡪࡷࠬᤍ"),
  bstack11ll1ll_opy_ (u"ࠩࡵࡩࡸ࡫ࡲࡷࡧࡇࡩࡻ࡯ࡣࡦࠩᤎ"),
  bstack11ll1ll_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪᤏ"),
  bstack11ll1ll_opy_ (u"ࠫࡸ࡫࡮ࡥࡍࡨࡽࡸ࠭ᤐ"),
  bstack11ll1ll_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡕࡧࡳࡴࡥࡲࡨࡪ࠭ᤑ"),
  bstack11ll1ll_opy_ (u"࠭ࡵࡱࡦࡤࡸࡪࡏ࡯ࡴࡆࡨࡺ࡮ࡩࡥࡔࡧࡷࡸ࡮ࡴࡧࡴࠩᤒ"),
  bstack11ll1ll_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡁࡶࡦ࡬ࡳࡎࡴࡪࡦࡥࡷ࡭ࡴࡴࠧᤓ"),
  bstack11ll1ll_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡂࡲࡳࡰࡪࡖࡡࡺࠩᤔ"),
  bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪᤕ"),
  bstack11ll1ll_opy_ (u"ࠪࡻࡩ࡯࡯ࡔࡧࡵࡺ࡮ࡩࡥࠨᤖ"),
  bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ᤗ"),
  bstack11ll1ll_opy_ (u"ࠬࡶࡲࡦࡸࡨࡲࡹࡉࡲࡰࡵࡶࡗ࡮ࡺࡥࡕࡴࡤࡧࡰ࡯࡮ࡨࠩᤘ"),
  bstack11ll1ll_opy_ (u"࠭ࡨࡪࡩ࡫ࡇࡴࡴࡴࡳࡣࡶࡸࠬᤙ"),
  bstack11ll1ll_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡐࡳࡧࡩࡩࡷ࡫࡮ࡤࡧࡶࠫᤚ"),
  bstack11ll1ll_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡔ࡫ࡰࠫᤛ"),
  bstack11ll1ll_opy_ (u"ࠩࡶ࡭ࡲࡕࡰࡵ࡫ࡲࡲࡸ࠭ᤜ"),
  bstack11ll1ll_opy_ (u"ࠪࡶࡪࡳ࡯ࡷࡧࡌࡓࡘࡇࡰࡱࡕࡨࡸࡹ࡯࡮ࡨࡵࡏࡳࡨࡧ࡬ࡪࡼࡤࡸ࡮ࡵ࡮ࠨᤝ"),
  bstack11ll1ll_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭ᤞ"),
  bstack11ll1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ᤟"),
  bstack11ll1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠨᤠ"),
  bstack11ll1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭ᤡ"),
  bstack11ll1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪᤢ"),
  bstack11ll1ll_opy_ (u"ࠩࡳࡥ࡬࡫ࡌࡰࡣࡧࡗࡹࡸࡡࡵࡧࡪࡽࠬᤣ"),
  bstack11ll1ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩᤤ"),
  bstack11ll1ll_opy_ (u"ࠫࡹ࡯࡭ࡦࡱࡸࡸࡸ࠭ᤥ"),
  bstack11ll1ll_opy_ (u"ࠬࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡑࡴࡲࡱࡵࡺࡂࡦࡪࡤࡺ࡮ࡵࡲࠨᤦ")
]
bstack11ll111l11_opy_ = {
  bstack11ll1ll_opy_ (u"࠭ࡶࠨᤧ"): bstack11ll1ll_opy_ (u"ࠧࡷࠩᤨ"),
  bstack11ll1ll_opy_ (u"ࠨࡨࠪᤩ"): bstack11ll1ll_opy_ (u"ࠩࡩࠫᤪ"),
  bstack11ll1ll_opy_ (u"ࠪࡪࡴࡸࡣࡦࠩᤫ"): bstack11ll1ll_opy_ (u"ࠫ࡫ࡵࡲࡤࡧࠪ᤬"),
  bstack11ll1ll_opy_ (u"ࠬࡵ࡮࡭ࡻࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ᤭"): bstack11ll1ll_opy_ (u"࠭࡯࡯࡮ࡼࡅࡺࡺ࡯࡮ࡣࡷࡩࠬ᤮"),
  bstack11ll1ll_opy_ (u"ࠧࡧࡱࡵࡧࡪࡲ࡯ࡤࡣ࡯ࠫ᤯"): bstack11ll1ll_opy_ (u"ࠨࡨࡲࡶࡨ࡫࡬ࡰࡥࡤࡰࠬᤰ"),
  bstack11ll1ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡩࡱࡶࡸࠬᤱ"): bstack11ll1ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡊࡲࡷࡹ࠭ᤲ"),
  bstack11ll1ll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡳࡳࡷࡺࠧᤳ"): bstack11ll1ll_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡴࡸࡴࠨᤴ"),
  bstack11ll1ll_opy_ (u"࠭ࡰࡳࡱࡻࡽࡺࡹࡥࡳࠩᤵ"): bstack11ll1ll_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡛ࡳࡦࡴࠪᤶ"),
  bstack11ll1ll_opy_ (u"ࠨࡲࡵࡳࡽࡿࡰࡢࡵࡶࠫᤷ"): bstack11ll1ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡣࡶࡷࠬᤸ"),
  bstack11ll1ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡲࡵࡳࡽࡿࡨࡰࡵࡷ᤹ࠫ"): bstack11ll1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡉࡱࡶࡸࠬ᤺"),
  bstack11ll1ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡴࡷࡵࡸࡺࡲࡲࡶࡹ᤻࠭"): bstack11ll1ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡓࡳࡷࡺࠧ᤼"),
  bstack11ll1ll_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡶࡲࡰࡺࡼࡹࡸ࡫ࡲࠨ᤽"): bstack11ll1ll_opy_ (u"ࠨ࠯࡯ࡳࡨࡧ࡬ࡑࡴࡲࡼࡾ࡛ࡳࡦࡴࠪ᤾"),
  bstack11ll1ll_opy_ (u"ࠩ࠰ࡰࡴࡩࡡ࡭ࡲࡵࡳࡽࡿࡵࡴࡧࡵࠫ᤿"): bstack11ll1ll_opy_ (u"ࠪ࠱ࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡖࡵࡨࡶࠬ᥀"),
  bstack11ll1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡳࡶࡴࡾࡹࡱࡣࡶࡷࠬ᥁"): bstack11ll1ll_opy_ (u"ࠬ࠳࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡓࡥࡸࡹࠧ᥂"),
  bstack11ll1ll_opy_ (u"࠭࠭࡭ࡱࡦࡥࡱࡶࡲࡰࡺࡼࡴࡦࡹࡳࠨ᥃"): bstack11ll1ll_opy_ (u"ࠧ࠮࡮ࡲࡧࡦࡲࡐࡳࡱࡻࡽࡕࡧࡳࡴࠩ᥄"),
  bstack11ll1ll_opy_ (u"ࠨࡤ࡬ࡲࡦࡸࡹࡱࡣࡷ࡬ࠬ᥅"): bstack11ll1ll_opy_ (u"ࠩࡥ࡭ࡳࡧࡲࡺࡲࡤࡸ࡭࠭᥆"),
  bstack11ll1ll_opy_ (u"ࠪࡴࡦࡩࡦࡪ࡮ࡨࠫ᥇"): bstack11ll1ll_opy_ (u"ࠫ࠲ࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧ᥈"),
  bstack11ll1ll_opy_ (u"ࠬࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧ᥉"): bstack11ll1ll_opy_ (u"࠭࠭ࡱࡣࡦ࠱࡫࡯࡬ࡦࠩ᥊"),
  bstack11ll1ll_opy_ (u"ࠧ࠮ࡲࡤࡧ࠲࡬ࡩ࡭ࡧࠪ᥋"): bstack11ll1ll_opy_ (u"ࠨ࠯ࡳࡥࡨ࠳ࡦࡪ࡮ࡨࠫ᥌"),
  bstack11ll1ll_opy_ (u"ࠩ࡯ࡳ࡬࡬ࡩ࡭ࡧࠪ᥍"): bstack11ll1ll_opy_ (u"ࠪࡰࡴ࡭ࡦࡪ࡮ࡨࠫ᥎"),
  bstack11ll1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭᥏"): bstack11ll1ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᥐ"),
  bstack11ll1ll_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲ࠳ࡲࡦࡲࡨࡥࡹ࡫ࡲࠨᥑ"): bstack11ll1ll_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡲࡨࡥࡹ࡫ࡲࠨᥒ")
}
bstack11l11lll1ll_opy_ = bstack11ll1ll_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࡪ࡭ࡹ࡮ࡵࡣ࠰ࡦࡳࡲ࠵ࡰࡦࡴࡦࡽ࠴ࡩ࡬ࡪ࠱ࡵࡩࡱ࡫ࡡࡴࡧࡶ࠳ࡱࡧࡴࡦࡵࡷ࠳ࡩࡵࡷ࡯࡮ࡲࡥࡩࠨᥓ")
bstack11l1l11l11l_opy_ = bstack11ll1ll_opy_ (u"ࠤ࠲ࡴࡪࡸࡣࡺ࠱࡫ࡩࡦࡲࡴࡩࡥ࡫ࡩࡨࡱࠢᥔ")
bstack11lllll11_opy_ = bstack11ll1ll_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡪࡪࡳ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡸ࡫࡮ࡥࡡࡶࡨࡰࡥࡥࡷࡧࡱࡸࡸࠨᥕ")
bstack11lll111ll_opy_ = bstack11ll1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴࡮ࡵࡣ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡽࡤ࠰ࡪࡸࡦࠬᥖ")
bstack1l1l1lllll_opy_ = bstack11ll1ll_opy_ (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴࡮ࡵࡣ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠨᥗ")
bstack11llll1l1l_opy_ = bstack11ll1ll_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡩࡷࡥ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯࡯ࡧࡻࡸࡤ࡮ࡵࡣࡵࠪᥘ")
bstack1l1ll1l11_opy_ = {
  bstack11ll1ll_opy_ (u"ࠧࡥࡧࡩࡥࡺࡲࡴࠨᥙ"): bstack11ll1ll_opy_ (u"ࠨࡪࡸࡦ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨᥚ"),
  bstack11ll1ll_opy_ (u"ࠩࡸࡷ࠲࡫ࡡࡴࡶࠪᥛ"): bstack11ll1ll_opy_ (u"ࠪ࡬ࡺࡨ࠭ࡶࡵࡨ࠱ࡴࡴ࡬ࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬᥜ"),
  bstack11ll1ll_opy_ (u"ࠫࡺࡹࠧᥝ"): bstack11ll1ll_opy_ (u"ࠬ࡮ࡵࡣ࠯ࡸࡷ࠲ࡵ࡮࡭ࡻ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ᥞ"),
  bstack11ll1ll_opy_ (u"࠭ࡥࡶࠩᥟ"): bstack11ll1ll_opy_ (u"ࠧࡩࡷࡥ࠱ࡪࡻ࠭ࡰࡰ࡯ࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨᥠ"),
  bstack11ll1ll_opy_ (u"ࠨ࡫ࡱࠫᥡ"): bstack11ll1ll_opy_ (u"ࠩ࡫ࡹࡧ࠳ࡡࡱࡵ࠰ࡳࡳࡲࡹ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫᥢ"),
  bstack11ll1ll_opy_ (u"ࠪࡥࡺ࠭ᥣ"): bstack11ll1ll_opy_ (u"ࠫ࡭ࡻࡢ࠮ࡣࡳࡷࡪ࠳࡯࡯࡮ࡼ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧᥤ")
}
bstack11l1l111ll1_opy_ = {
  bstack11ll1ll_opy_ (u"ࠬࡩࡲࡪࡶ࡬ࡧࡦࡲࠧᥥ"): 50,
  bstack11ll1ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᥦ"): 40,
  bstack11ll1ll_opy_ (u"ࠧࡸࡣࡵࡲ࡮ࡴࡧࠨᥧ"): 30,
  bstack11ll1ll_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭ᥨ"): 20,
  bstack11ll1ll_opy_ (u"ࠩࡧࡩࡧࡻࡧࠨᥩ"): 10
}
bstack11l111lll_opy_ = bstack11l1l111ll1_opy_[bstack11ll1ll_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨᥪ")]
bstack1111l111ll_opy_ = bstack11ll1ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠱ࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࠪᥫ")
bstack1l1111l1l_opy_ = bstack11ll1ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱ࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࠪᥬ")
bstack11lll11l11_opy_ = bstack11ll1ll_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠳ࡰࡺࡶ࡫ࡳࡳࡧࡧࡦࡰࡷ࠳ࠬᥭ")
bstack1ll11l1ll1_opy_ = bstack11ll1ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡱࡻࡷ࡬ࡴࡴࡡࡨࡧࡱࡸ࠴࠭᥮")
bstack1111ll11_opy_ = bstack11ll1ll_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵࠢࡤࡲࡩࠦࡰࡺࡶࡨࡷࡹ࠳ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠡࡲࡤࡧࡰࡧࡧࡦࡵ࠱ࠤࡥࡶࡩࡱࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶࠣࡴࡾࡺࡥࡴࡶ࠰ࡷࡪࡲࡥ࡯࡫ࡸࡱࡥ࠭᥯")
bstack11l11l1l1ll_opy_ = [bstack11ll1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡗࡖࡉࡗࡔࡁࡎࡇࠪᥰ"), bstack11ll1ll_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡗࡖࡉࡗࡔࡁࡎࡇࠪᥱ")]
bstack11l11llllll_opy_ = [bstack11ll1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅࡈࡉࡅࡔࡕࡢࡏࡊ࡟ࠧᥲ"), bstack11ll1ll_opy_ (u"ࠬ࡟ࡏࡖࡔࡢࡅࡈࡉࡅࡔࡕࡢࡏࡊ࡟ࠧᥳ")]
bstack1l1l1l1111_opy_ = re.compile(bstack11ll1ll_opy_ (u"࠭࡞࡜࡞࡟ࡻ࠲ࡣࠫ࠻࠰࠭ࠨࠬᥴ"))
bstack1llll1l11l_opy_ = [
  bstack11ll1ll_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡒࡦࡳࡥࠨ᥵"),
  bstack11ll1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ᥶"),
  bstack11ll1ll_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭᥷"),
  bstack11ll1ll_opy_ (u"ࠪࡲࡪࡽࡃࡰ࡯ࡰࡥࡳࡪࡔࡪ࡯ࡨࡳࡺࡺࠧ᥸"),
  bstack11ll1ll_opy_ (u"ࠫࡦࡶࡰࠨ᥹"),
  bstack11ll1ll_opy_ (u"ࠬࡻࡤࡪࡦࠪ᥺"),
  bstack11ll1ll_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࠨ᥻"),
  bstack11ll1ll_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࡫ࠧ᥼"),
  bstack11ll1ll_opy_ (u"ࠨࡱࡵ࡭ࡪࡴࡴࡢࡶ࡬ࡳࡳ࠭᥽"),
  bstack11ll1ll_opy_ (u"ࠩࡤࡹࡹࡵࡗࡦࡤࡹ࡭ࡪࡽࠧ᥾"),
  bstack11ll1ll_opy_ (u"ࠪࡲࡴࡘࡥࡴࡧࡷࠫ᥿"), bstack11ll1ll_opy_ (u"ࠫ࡫ࡻ࡬࡭ࡔࡨࡷࡪࡺࠧᦀ"),
  bstack11ll1ll_opy_ (u"ࠬࡩ࡬ࡦࡣࡵࡗࡾࡹࡴࡦ࡯ࡉ࡭ࡱ࡫ࡳࠨᦁ"),
  bstack11ll1ll_opy_ (u"࠭ࡥࡷࡧࡱࡸ࡙࡯࡭ࡪࡰࡪࡷࠬᦂ"),
  bstack11ll1ll_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡐࡦࡴࡩࡳࡷࡳࡡ࡯ࡥࡨࡐࡴ࡭ࡧࡪࡰࡪࠫᦃ"),
  bstack11ll1ll_opy_ (u"ࠨࡱࡷ࡬ࡪࡸࡁࡱࡲࡶࠫᦄ"),
  bstack11ll1ll_opy_ (u"ࠩࡳࡶ࡮ࡴࡴࡑࡣࡪࡩࡘࡵࡵࡳࡥࡨࡓࡳࡌࡩ࡯ࡦࡉࡥ࡮ࡲࡵࡳࡧࠪᦅ"),
  bstack11ll1ll_opy_ (u"ࠪࡥࡵࡶࡁࡤࡶ࡬ࡺ࡮ࡺࡹࠨᦆ"), bstack11ll1ll_opy_ (u"ࠫࡦࡶࡰࡑࡣࡦ࡯ࡦ࡭ࡥࠨᦇ"), bstack11ll1ll_opy_ (u"ࠬࡧࡰࡱ࡙ࡤ࡭ࡹࡇࡣࡵ࡫ࡹ࡭ࡹࡿࠧᦈ"), bstack11ll1ll_opy_ (u"࠭ࡡࡱࡲ࡚ࡥ࡮ࡺࡐࡢࡥ࡮ࡥ࡬࡫ࠧᦉ"), bstack11ll1ll_opy_ (u"ࠧࡢࡲࡳ࡛ࡦ࡯ࡴࡅࡷࡵࡥࡹ࡯࡯࡯ࠩᦊ"),
  bstack11ll1ll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡓࡧࡤࡨࡾ࡚ࡩ࡮ࡧࡲࡹࡹ࠭ᦋ"),
  bstack11ll1ll_opy_ (u"ࠩࡤࡰࡱࡵࡷࡕࡧࡶࡸࡕࡧࡣ࡬ࡣࡪࡩࡸ࠭ᦌ"),
  bstack11ll1ll_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࡇࡴࡼࡥࡳࡣࡪࡩࠬᦍ"), bstack11ll1ll_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࡈࡵࡶࡦࡴࡤ࡫ࡪࡋ࡮ࡥࡋࡱࡸࡪࡴࡴࠨᦎ"),
  bstack11ll1ll_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩࡊࡥࡷ࡫ࡦࡩࡗ࡫ࡡࡥࡻࡗ࡭ࡲ࡫࡯ࡶࡶࠪᦏ"),
  bstack11ll1ll_opy_ (u"࠭ࡡࡥࡤࡓࡳࡷࡺࠧᦐ"),
  bstack11ll1ll_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࡅࡧࡹ࡭ࡨ࡫ࡓࡰࡥ࡮ࡩࡹ࠭ᦑ"),
  bstack11ll1ll_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࡋࡱࡷࡹࡧ࡬࡭ࡖ࡬ࡱࡪࡵࡵࡵࠩᦒ"),
  bstack11ll1ll_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡌࡲࡸࡺࡡ࡭࡮ࡓࡥࡹ࡮ࠧᦓ"),
  bstack11ll1ll_opy_ (u"ࠪࡥࡻࡪࠧᦔ"), bstack11ll1ll_opy_ (u"ࠫࡦࡼࡤࡍࡣࡸࡲࡨ࡮ࡔࡪ࡯ࡨࡳࡺࡺࠧᦕ"), bstack11ll1ll_opy_ (u"ࠬࡧࡶࡥࡔࡨࡥࡩࡿࡔࡪ࡯ࡨࡳࡺࡺࠧᦖ"), bstack11ll1ll_opy_ (u"࠭ࡡࡷࡦࡄࡶ࡬ࡹࠧᦗ"),
  bstack11ll1ll_opy_ (u"ࠧࡶࡵࡨࡏࡪࡿࡳࡵࡱࡵࡩࠬᦘ"), bstack11ll1ll_opy_ (u"ࠨ࡭ࡨࡽࡸࡺ࡯ࡳࡧࡓࡥࡹ࡮ࠧᦙ"), bstack11ll1ll_opy_ (u"ࠩ࡮ࡩࡾࡹࡴࡰࡴࡨࡔࡦࡹࡳࡸࡱࡵࡨࠬᦚ"),
  bstack11ll1ll_opy_ (u"ࠪ࡯ࡪࡿࡁ࡭࡫ࡤࡷࠬᦛ"), bstack11ll1ll_opy_ (u"ࠫࡰ࡫ࡹࡑࡣࡶࡷࡼࡵࡲࡥࠩᦜ"),
  bstack11ll1ll_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡩࡸࡩࡷࡧࡵࡉࡽ࡫ࡣࡶࡶࡤࡦࡱ࡫ࠧᦝ"), bstack11ll1ll_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡪࡲࡪࡸࡨࡶࡆࡸࡧࡴࠩᦞ"), bstack11ll1ll_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷࡋࡸࡦࡥࡸࡸࡦࡨ࡬ࡦࡆ࡬ࡶࠬᦟ"), bstack11ll1ll_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡥࡴ࡬ࡺࡪࡸࡃࡩࡴࡲࡱࡪࡓࡡࡱࡲ࡬ࡲ࡬ࡌࡩ࡭ࡧࠪᦠ"), bstack11ll1ll_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡦࡵ࡭ࡻ࡫ࡲࡖࡵࡨࡗࡾࡹࡴࡦ࡯ࡈࡼࡪࡩࡵࡵࡣࡥࡰࡪ࠭ᦡ"),
  bstack11ll1ll_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡧࡶ࡮ࡼࡥࡳࡒࡲࡶࡹ࠭ᦢ"), bstack11ll1ll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡨࡷ࡯ࡶࡦࡴࡓࡳࡷࡺࡳࠨᦣ"),
  bstack11ll1ll_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡩࡸࡩࡷࡧࡵࡈ࡮ࡹࡡࡣ࡮ࡨࡆࡺ࡯࡬ࡥࡅ࡫ࡩࡨࡱࠧᦤ"),
  bstack11ll1ll_opy_ (u"࠭ࡡࡶࡶࡲ࡛ࡪࡨࡶࡪࡧࡺࡘ࡮ࡳࡥࡰࡷࡷࠫᦥ"),
  bstack11ll1ll_opy_ (u"ࠧࡪࡰࡷࡩࡳࡺࡁࡤࡶ࡬ࡳࡳ࠭ᦦ"), bstack11ll1ll_opy_ (u"ࠨ࡫ࡱࡸࡪࡴࡴࡄࡣࡷࡩ࡬ࡵࡲࡺࠩᦧ"), bstack11ll1ll_opy_ (u"ࠩ࡬ࡲࡹ࡫࡮ࡵࡈ࡯ࡥ࡬ࡹࠧᦨ"), bstack11ll1ll_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡤࡰࡎࡴࡴࡦࡰࡷࡅࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᦩ"),
  bstack11ll1ll_opy_ (u"ࠫࡩࡵ࡮ࡵࡕࡷࡳࡵࡇࡰࡱࡑࡱࡖࡪࡹࡥࡵࠩᦪ"),
  bstack11ll1ll_opy_ (u"ࠬࡻ࡮ࡪࡥࡲࡨࡪࡑࡥࡺࡤࡲࡥࡷࡪࠧᦫ"), bstack11ll1ll_opy_ (u"࠭ࡲࡦࡵࡨࡸࡐ࡫ࡹࡣࡱࡤࡶࡩ࠭᦬"),
  bstack11ll1ll_opy_ (u"ࠧ࡯ࡱࡖ࡭࡬ࡴࠧ᦭"),
  bstack11ll1ll_opy_ (u"ࠨ࡫ࡪࡲࡴࡸࡥࡖࡰ࡬ࡱࡵࡵࡲࡵࡣࡱࡸ࡛࡯ࡥࡸࡵࠪ᦮"),
  bstack11ll1ll_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡲࡩࡸ࡯ࡪࡦ࡚ࡥࡹࡩࡨࡦࡴࡶࠫ᦯"),
  bstack11ll1ll_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᦰ"),
  bstack11ll1ll_opy_ (u"ࠫࡷ࡫ࡣࡳࡧࡤࡸࡪࡉࡨࡳࡱࡰࡩࡉࡸࡩࡷࡧࡵࡗࡪࡹࡳࡪࡱࡱࡷࠬᦱ"),
  bstack11ll1ll_opy_ (u"ࠬࡴࡡࡵ࡫ࡹࡩ࡜࡫ࡢࡔࡥࡵࡩࡪࡴࡳࡩࡱࡷࠫᦲ"),
  bstack11ll1ll_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࡓࡤࡴࡨࡩࡳࡹࡨࡰࡶࡓࡥࡹ࡮ࠧᦳ"),
  bstack11ll1ll_opy_ (u"ࠧ࡯ࡧࡷࡻࡴࡸ࡫ࡔࡲࡨࡩࡩ࠭ᦴ"),
  bstack11ll1ll_opy_ (u"ࠨࡩࡳࡷࡊࡴࡡࡣ࡮ࡨࡨࠬᦵ"),
  bstack11ll1ll_opy_ (u"ࠩ࡬ࡷࡍ࡫ࡡࡥ࡮ࡨࡷࡸ࠭ᦶ"),
  bstack11ll1ll_opy_ (u"ࠪࡥࡩࡨࡅࡹࡧࡦࡘ࡮ࡳࡥࡰࡷࡷࠫᦷ"),
  bstack11ll1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡨࡗࡨࡸࡩࡱࡶࠪᦸ"),
  bstack11ll1ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡇࡩࡻ࡯ࡣࡦࡋࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡥࡹ࡯࡯࡯ࠩᦹ"),
  bstack11ll1ll_opy_ (u"࠭ࡡࡶࡶࡲࡋࡷࡧ࡮ࡵࡒࡨࡶࡲ࡯ࡳࡴ࡫ࡲࡲࡸ࠭ᦺ"),
  bstack11ll1ll_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࡏࡣࡷࡹࡷࡧ࡬ࡐࡴ࡬ࡩࡳࡺࡡࡵ࡫ࡲࡲࠬᦻ"),
  bstack11ll1ll_opy_ (u"ࠨࡵࡼࡷࡹ࡫࡭ࡑࡱࡵࡸࠬᦼ"),
  bstack11ll1ll_opy_ (u"ࠩࡵࡩࡲࡵࡴࡦࡃࡧࡦࡍࡵࡳࡵࠩᦽ"),
  bstack11ll1ll_opy_ (u"ࠪࡷࡰ࡯ࡰࡖࡰ࡯ࡳࡨࡱࠧᦾ"), bstack11ll1ll_opy_ (u"ࠫࡺࡴ࡬ࡰࡥ࡮ࡘࡾࡶࡥࠨᦿ"), bstack11ll1ll_opy_ (u"ࠬࡻ࡮࡭ࡱࡦ࡯ࡐ࡫ࡹࠨᧀ"),
  bstack11ll1ll_opy_ (u"࠭ࡡࡶࡶࡲࡐࡦࡻ࡮ࡤࡪࠪᧁ"),
  bstack11ll1ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡑࡵࡧࡤࡣࡷࡇࡦࡶࡴࡶࡴࡨࠫᧂ"),
  bstack11ll1ll_opy_ (u"ࠨࡷࡱ࡭ࡳࡹࡴࡢ࡮࡯ࡓࡹ࡮ࡥࡳࡒࡤࡧࡰࡧࡧࡦࡵࠪᧃ"),
  bstack11ll1ll_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧ࡚࡭ࡳࡪ࡯ࡸࡃࡱ࡭ࡲࡧࡴࡪࡱࡱࠫᧄ"),
  bstack11ll1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡖࡲࡳࡱࡹࡖࡦࡴࡶ࡭ࡴࡴࠧᧅ"),
  bstack11ll1ll_opy_ (u"ࠫࡪࡴࡦࡰࡴࡦࡩࡆࡶࡰࡊࡰࡶࡸࡦࡲ࡬ࠨᧆ"),
  bstack11ll1ll_opy_ (u"ࠬ࡫࡮ࡴࡷࡵࡩ࡜࡫ࡢࡷ࡫ࡨࡻࡸࡎࡡࡷࡧࡓࡥ࡬࡫ࡳࠨᧇ"), bstack11ll1ll_opy_ (u"࠭ࡷࡦࡤࡹ࡭ࡪࡽࡄࡦࡸࡷࡳࡴࡲࡳࡑࡱࡵࡸࠬᧈ"), bstack11ll1ll_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡗࡦࡤࡹ࡭ࡪࡽࡄࡦࡶࡤ࡭ࡱࡹࡃࡰ࡮࡯ࡩࡨࡺࡩࡰࡰࠪᧉ"),
  bstack11ll1ll_opy_ (u"ࠨࡴࡨࡱࡴࡺࡥࡂࡲࡳࡷࡈࡧࡣࡩࡧࡏ࡭ࡲ࡯ࡴࠨ᧊"),
  bstack11ll1ll_opy_ (u"ࠩࡦࡥࡱ࡫࡮ࡥࡣࡵࡊࡴࡸ࡭ࡢࡶࠪ᧋"),
  bstack11ll1ll_opy_ (u"ࠪࡦࡺࡴࡤ࡭ࡧࡌࡨࠬ᧌"),
  bstack11ll1ll_opy_ (u"ࠫࡱࡧࡵ࡯ࡥ࡫ࡘ࡮ࡳࡥࡰࡷࡷࠫ᧍"),
  bstack11ll1ll_opy_ (u"ࠬࡲ࡯ࡤࡣࡷ࡭ࡴࡴࡓࡦࡴࡹ࡭ࡨ࡫ࡳࡆࡰࡤࡦࡱ࡫ࡤࠨ᧎"), bstack11ll1ll_opy_ (u"࠭࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࡔࡧࡵࡺ࡮ࡩࡥࡴࡃࡸࡸ࡭ࡵࡲࡪࡼࡨࡨࠬ᧏"),
  bstack11ll1ll_opy_ (u"ࠧࡢࡷࡷࡳࡆࡩࡣࡦࡲࡷࡅࡱ࡫ࡲࡵࡵࠪ᧐"), bstack11ll1ll_opy_ (u"ࠨࡣࡸࡸࡴࡊࡩࡴ࡯࡬ࡷࡸࡇ࡬ࡦࡴࡷࡷࠬ᧑"),
  bstack11ll1ll_opy_ (u"ࠩࡱࡥࡹ࡯ࡶࡦࡋࡱࡷࡹࡸࡵ࡮ࡧࡱࡸࡸࡒࡩࡣࠩ᧒"),
  bstack11ll1ll_opy_ (u"ࠪࡲࡦࡺࡩࡷࡧ࡚ࡩࡧ࡚ࡡࡱࠩ᧓"),
  bstack11ll1ll_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࡍࡳ࡯ࡴࡪࡣ࡯࡙ࡷࡲࠧ᧔"), bstack11ll1ll_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࡆࡲ࡬ࡰࡹࡓࡳࡵࡻࡰࡴࠩ᧕"), bstack11ll1ll_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮ࡏࡧ࡯ࡱࡵࡩࡋࡸࡡࡶࡦ࡚ࡥࡷࡴࡩ࡯ࡩࠪ᧖"), bstack11ll1ll_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࡏࡱࡧࡱࡐ࡮ࡴ࡫ࡴࡋࡱࡆࡦࡩ࡫ࡨࡴࡲࡹࡳࡪࠧ᧗"),
  bstack11ll1ll_opy_ (u"ࠨ࡭ࡨࡩࡵࡑࡥࡺࡅ࡫ࡥ࡮ࡴࡳࠨ᧘"),
  bstack11ll1ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡪࡼࡤࡦࡱ࡫ࡓࡵࡴ࡬ࡲ࡬ࡹࡄࡪࡴࠪ᧙"),
  bstack11ll1ll_opy_ (u"ࠪࡴࡷࡵࡣࡦࡵࡶࡅࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭᧚"),
  bstack11ll1ll_opy_ (u"ࠫ࡮ࡴࡴࡦࡴࡎࡩࡾࡊࡥ࡭ࡣࡼࠫ᧛"),
  bstack11ll1ll_opy_ (u"ࠬࡹࡨࡰࡹࡌࡓࡘࡒ࡯ࡨࠩ᧜"),
  bstack11ll1ll_opy_ (u"࠭ࡳࡦࡰࡧࡏࡪࡿࡓࡵࡴࡤࡸࡪ࡭ࡹࠨ᧝"),
  bstack11ll1ll_opy_ (u"ࠧࡸࡧࡥ࡯࡮ࡺࡒࡦࡵࡳࡳࡳࡹࡥࡕ࡫ࡰࡩࡴࡻࡴࠨ᧞"), bstack11ll1ll_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸ࡜ࡧࡩࡵࡖ࡬ࡱࡪࡵࡵࡵࠩ᧟"),
  bstack11ll1ll_opy_ (u"ࠩࡵࡩࡲࡵࡴࡦࡆࡨࡦࡺ࡭ࡐࡳࡱࡻࡽࠬ᧠"),
  bstack11ll1ll_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡄࡷࡾࡴࡣࡆࡺࡨࡧࡺࡺࡥࡇࡴࡲࡱࡍࡺࡴࡱࡵࠪ᧡"),
  bstack11ll1ll_opy_ (u"ࠫࡸࡱࡩࡱࡎࡲ࡫ࡈࡧࡰࡵࡷࡵࡩࠬ᧢"),
  bstack11ll1ll_opy_ (u"ࠬࡽࡥࡣ࡭࡬ࡸࡉ࡫ࡢࡶࡩࡓࡶࡴࡾࡹࡑࡱࡵࡸࠬ᧣"),
  bstack11ll1ll_opy_ (u"࠭ࡦࡶ࡮࡯ࡇࡴࡴࡴࡦࡺࡷࡐ࡮ࡹࡴࠨ᧤"),
  bstack11ll1ll_opy_ (u"ࠧࡸࡣ࡬ࡸࡋࡵࡲࡂࡲࡳࡗࡨࡸࡩࡱࡶࠪ᧥"),
  bstack11ll1ll_opy_ (u"ࠨࡹࡨࡦࡻ࡯ࡥࡸࡅࡲࡲࡳ࡫ࡣࡵࡔࡨࡸࡷ࡯ࡥࡴࠩ᧦"),
  bstack11ll1ll_opy_ (u"ࠩࡤࡴࡵࡔࡡ࡮ࡧࠪ᧧"),
  bstack11ll1ll_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡖࡗࡑࡉࡥࡳࡶࠪ᧨"),
  bstack11ll1ll_opy_ (u"ࠫࡹࡧࡰࡘ࡫ࡷ࡬ࡘ࡮࡯ࡳࡶࡓࡶࡪࡹࡳࡅࡷࡵࡥࡹ࡯࡯࡯ࠩ᧩"),
  bstack11ll1ll_opy_ (u"ࠬࡹࡣࡢ࡮ࡨࡊࡦࡩࡴࡰࡴࠪ᧪"),
  bstack11ll1ll_opy_ (u"࠭ࡷࡥࡣࡏࡳࡨࡧ࡬ࡑࡱࡵࡸࠬ᧫"),
  bstack11ll1ll_opy_ (u"ࠧࡴࡪࡲࡻ࡝ࡩ࡯ࡥࡧࡏࡳ࡬࠭᧬"),
  bstack11ll1ll_opy_ (u"ࠨ࡫ࡲࡷࡎࡴࡳࡵࡣ࡯ࡰࡕࡧࡵࡴࡧࠪ᧭"),
  bstack11ll1ll_opy_ (u"ࠩࡻࡧࡴࡪࡥࡄࡱࡱࡪ࡮࡭ࡆࡪ࡮ࡨࠫ᧮"),
  bstack11ll1ll_opy_ (u"ࠪ࡯ࡪࡿࡣࡩࡣ࡬ࡲࡕࡧࡳࡴࡹࡲࡶࡩ࠭᧯"),
  bstack11ll1ll_opy_ (u"ࠫࡺࡹࡥࡑࡴࡨࡦࡺ࡯࡬ࡵ࡙ࡇࡅࠬ᧰"),
  bstack11ll1ll_opy_ (u"ࠬࡶࡲࡦࡸࡨࡲࡹ࡝ࡄࡂࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠭᧱"),
  bstack11ll1ll_opy_ (u"࠭ࡷࡦࡤࡇࡶ࡮ࡼࡥࡳࡃࡪࡩࡳࡺࡕࡳ࡮ࠪ᧲"),
  bstack11ll1ll_opy_ (u"ࠧ࡬ࡧࡼࡧ࡭ࡧࡩ࡯ࡒࡤࡸ࡭࠭᧳"),
  bstack11ll1ll_opy_ (u"ࠨࡷࡶࡩࡓ࡫ࡷࡘࡆࡄࠫ᧴"),
  bstack11ll1ll_opy_ (u"ࠩࡺࡨࡦࡒࡡࡶࡰࡦ࡬࡙࡯࡭ࡦࡱࡸࡸࠬ᧵"), bstack11ll1ll_opy_ (u"ࠪࡻࡩࡧࡃࡰࡰࡱࡩࡨࡺࡩࡰࡰࡗ࡭ࡲ࡫࡯ࡶࡶࠪ᧶"),
  bstack11ll1ll_opy_ (u"ࠫࡽࡩ࡯ࡥࡧࡒࡶ࡬ࡏࡤࠨ᧷"), bstack11ll1ll_opy_ (u"ࠬࡾࡣࡰࡦࡨࡗ࡮࡭࡮ࡪࡰࡪࡍࡩ࠭᧸"),
  bstack11ll1ll_opy_ (u"࠭ࡵࡱࡦࡤࡸࡪࡪࡗࡅࡃࡅࡹࡳࡪ࡬ࡦࡋࡧࠫ᧹"),
  bstack11ll1ll_opy_ (u"ࠧࡳࡧࡶࡩࡹࡕ࡮ࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡶࡹࡕ࡮࡭ࡻࠪ᧺"),
  bstack11ll1ll_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡖ࡬ࡱࡪࡵࡵࡵࡵࠪ᧻"),
  bstack11ll1ll_opy_ (u"ࠩࡺࡨࡦ࡙ࡴࡢࡴࡷࡹࡵࡘࡥࡵࡴ࡬ࡩࡸ࠭᧼"), bstack11ll1ll_opy_ (u"ࠪࡻࡩࡧࡓࡵࡣࡵࡸࡺࡶࡒࡦࡶࡵࡽࡎࡴࡴࡦࡴࡹࡥࡱ࠭᧽"),
  bstack11ll1ll_opy_ (u"ࠫࡨࡵ࡮࡯ࡧࡦࡸࡍࡧࡲࡥࡹࡤࡶࡪࡑࡥࡺࡤࡲࡥࡷࡪࠧ᧾"),
  bstack11ll1ll_opy_ (u"ࠬࡳࡡࡹࡖࡼࡴ࡮ࡴࡧࡇࡴࡨࡵࡺ࡫࡮ࡤࡻࠪ᧿"),
  bstack11ll1ll_opy_ (u"࠭ࡳࡪ࡯ࡳࡰࡪࡏࡳࡗ࡫ࡶ࡭ࡧࡲࡥࡄࡪࡨࡧࡰ࠭ᨀ"),
  bstack11ll1ll_opy_ (u"ࠧࡶࡵࡨࡇࡦࡸࡴࡩࡣࡪࡩࡘࡹ࡬ࠨᨁ"),
  bstack11ll1ll_opy_ (u"ࠨࡵ࡫ࡳࡺࡲࡤࡖࡵࡨࡗ࡮ࡴࡧ࡭ࡧࡷࡳࡳ࡚ࡥࡴࡶࡐࡥࡳࡧࡧࡦࡴࠪᨂ"),
  bstack11ll1ll_opy_ (u"ࠩࡶࡸࡦࡸࡴࡊ࡙ࡇࡔࠬᨃ"),
  bstack11ll1ll_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡖࡲࡹࡨ࡮ࡉࡥࡇࡱࡶࡴࡲ࡬ࠨᨄ"),
  bstack11ll1ll_opy_ (u"ࠫ࡮࡭࡮ࡰࡴࡨࡌ࡮ࡪࡤࡦࡰࡄࡴ࡮ࡖ࡯࡭࡫ࡦࡽࡊࡸࡲࡰࡴࠪᨅ"),
  bstack11ll1ll_opy_ (u"ࠬࡳ࡯ࡤ࡭ࡏࡳࡨࡧࡴࡪࡱࡱࡅࡵࡶࠧᨆ"),
  bstack11ll1ll_opy_ (u"࠭࡬ࡰࡩࡦࡥࡹࡌ࡯ࡳ࡯ࡤࡸࠬᨇ"), bstack11ll1ll_opy_ (u"ࠧ࡭ࡱࡪࡧࡦࡺࡆࡪ࡮ࡷࡩࡷ࡙ࡰࡦࡥࡶࠫᨈ"),
  bstack11ll1ll_opy_ (u"ࠨࡣ࡯ࡰࡴࡽࡄࡦ࡮ࡤࡽࡆࡪࡢࠨᨉ"),
  bstack11ll1ll_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡌࡨࡑࡵࡣࡢࡶࡲࡶࡆࡻࡴࡰࡥࡲࡱࡵࡲࡥࡵ࡫ࡲࡲࠬᨊ")
]
bstack1ll11llll1_opy_ = bstack11ll1ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡦࡶࡩ࠮ࡥ࡯ࡳࡺࡪ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦ࠱ࡸࡴࡱࡵࡡࡥࠩᨋ")
bstack1l11l1ll1l_opy_ = [bstack11ll1ll_opy_ (u"ࠫ࠳ࡧࡰ࡬ࠩᨌ"), bstack11ll1ll_opy_ (u"ࠬ࠴ࡡࡢࡤࠪᨍ"), bstack11ll1ll_opy_ (u"࠭࠮ࡪࡲࡤࠫᨎ")]
bstack11l1l111l_opy_ = [bstack11ll1ll_opy_ (u"ࠧࡪࡦࠪᨏ"), bstack11ll1ll_opy_ (u"ࠨࡲࡤࡸ࡭࠭ᨐ"), bstack11ll1ll_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡡ࡬ࡨࠬᨑ"), bstack11ll1ll_opy_ (u"ࠪࡷ࡭ࡧࡲࡦࡣࡥࡰࡪࡥࡩࡥࠩᨒ")]
bstack11llllll11_opy_ = {
  bstack11ll1ll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫᨓ"): bstack11ll1ll_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᨔ"),
  bstack11ll1ll_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧᨕ"): bstack11ll1ll_opy_ (u"ࠧ࡮ࡱࡽ࠾࡫࡯ࡲࡦࡨࡲࡼࡔࡶࡴࡪࡱࡱࡷࠬᨖ"),
  bstack11ll1ll_opy_ (u"ࠨࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᨗ"): bstack11ll1ll_opy_ (u"ࠩࡰࡷ࠿࡫ࡤࡨࡧࡒࡴࡹ࡯࡯࡯ࡵᨘࠪ"),
  bstack11ll1ll_opy_ (u"ࠪ࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᨙ"): bstack11ll1ll_opy_ (u"ࠫࡸ࡫࠺ࡪࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᨚ"),
  bstack11ll1ll_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࡔࡶࡴࡪࡱࡱࡷࠬᨛ"): bstack11ll1ll_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧ᨜")
}
bstack11lll11l1l_opy_ = [
  bstack11ll1ll_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ᨝"),
  bstack11ll1ll_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭᨞"),
  bstack11ll1ll_opy_ (u"ࠩࡰࡷ࠿࡫ࡤࡨࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ᨟"),
  bstack11ll1ll_opy_ (u"ࠪࡷࡪࡀࡩࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᨠ"),
  bstack11ll1ll_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬᨡ"),
]
bstack1l1l1l11ll_opy_ = bstack11ll1llll1_opy_ + bstack11l1l111111_opy_ + bstack1llll1l11l_opy_
bstack11lll111l_opy_ = [
  bstack11ll1ll_opy_ (u"ࠬࡤ࡬ࡰࡥࡤࡰ࡭ࡵࡳࡵࠦࠪᨢ"),
  bstack11ll1ll_opy_ (u"࠭࡞ࡣࡵ࠰ࡰࡴࡩࡡ࡭࠰ࡦࡳࡲࠪࠧᨣ"),
  bstack11ll1ll_opy_ (u"ࠧ࡟࠳࠵࠻࠳࠭ᨤ"),
  bstack11ll1ll_opy_ (u"ࠨࡠ࠴࠴࠳࠭ᨥ"),
  bstack11ll1ll_opy_ (u"ࠩࡡ࠵࠼࠸࠮࠲࡝࠹࠱࠾ࡣ࠮ࠨᨦ"),
  bstack11ll1ll_opy_ (u"ࠪࡢ࠶࠽࠲࠯࠴࡞࠴࠲࠿࡝࠯ࠩᨧ"),
  bstack11ll1ll_opy_ (u"ࠫࡣ࠷࠷࠳࠰࠶࡟࠵࠳࠱࡞࠰ࠪᨨ"),
  bstack11ll1ll_opy_ (u"ࠬࡤ࠱࠺࠴࠱࠵࠻࠾࠮ࠨᨩ")
]
bstack11l11llll11_opy_ = bstack11ll1ll_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡢࡲ࡬࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧᨪ")
bstack1l11ll1ll1_opy_ = bstack11ll1ll_opy_ (u"ࠧࡴࡦ࡮࠳ࡻ࠷࠯ࡦࡸࡨࡲࡹ࠭ᨫ")
bstack11111llll1_opy_ = [ bstack11ll1ll_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪᨬ") ]
bstack1l111ll1l1_opy_ = [ bstack11ll1ll_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨᨭ") ]
bstack11111l1111_opy_ = [bstack11ll1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧᨮ")]
bstack1lll1llll1_opy_ = [ bstack11ll1ll_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫᨯ") ]
bstack11lll1111l_opy_ = bstack11ll1ll_opy_ (u"࡙ࠬࡄࡌࡕࡨࡸࡺࡶࠧᨰ")
bstack1l1l11l11_opy_ = bstack11ll1ll_opy_ (u"࠭ࡓࡅࡍࡗࡩࡸࡺࡁࡵࡶࡨࡱࡵࡺࡥࡥࠩᨱ")
bstack111ll1l11_opy_ = bstack11ll1ll_opy_ (u"ࠧࡔࡆࡎࡘࡪࡹࡴࡔࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࠫᨲ")
bstack111l1ll1l_opy_ = bstack11ll1ll_opy_ (u"ࠨ࠶࠱࠴࠳࠶ࠧᨳ")
bstack11lllll11l_opy_ = [
  bstack11ll1ll_opy_ (u"ࠩࡈࡖࡗࡥࡆࡂࡋࡏࡉࡉ࠭ᨴ"),
  bstack11ll1ll_opy_ (u"ࠪࡉࡗࡘ࡟ࡕࡋࡐࡉࡉࡥࡏࡖࡖࠪᨵ"),
  bstack11ll1ll_opy_ (u"ࠫࡊࡘࡒࡠࡄࡏࡓࡈࡑࡅࡅࡡࡅ࡝ࡤࡉࡌࡊࡇࡑࡘࠬᨶ"),
  bstack11ll1ll_opy_ (u"ࠬࡋࡒࡓࡡࡑࡉ࡙࡝ࡏࡓࡍࡢࡇࡍࡇࡎࡈࡇࡇࠫᨷ"),
  bstack11ll1ll_opy_ (u"࠭ࡅࡓࡔࡢࡗࡔࡉࡋࡆࡖࡢࡒࡔ࡚࡟ࡄࡑࡑࡒࡊࡉࡔࡆࡆࠪᨸ"),
  bstack11ll1ll_opy_ (u"ࠧࡆࡔࡕࡣࡈࡕࡎࡏࡇࡆࡘࡎࡕࡎࡠࡅࡏࡓࡘࡋࡄࠨᨹ"),
  bstack11ll1ll_opy_ (u"ࠨࡇࡕࡖࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡕࡉࡘࡋࡔࠨᨺ"),
  bstack11ll1ll_opy_ (u"ࠩࡈࡖࡗࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡖࡊࡌࡕࡔࡇࡇࠫᨻ"),
  bstack11ll1ll_opy_ (u"ࠪࡉࡗࡘ࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣࡆࡈࡏࡓࡖࡈࡈࠬᨼ"),
  bstack11ll1ll_opy_ (u"ࠫࡊࡘࡒࡠࡅࡒࡒࡓࡋࡃࡕࡋࡒࡒࡤࡌࡁࡊࡎࡈࡈࠬᨽ"),
  bstack11ll1ll_opy_ (u"ࠬࡋࡒࡓࡡࡑࡅࡒࡋ࡟ࡏࡑࡗࡣࡗࡋࡓࡐࡎ࡙ࡉࡉ࠭ᨾ"),
  bstack11ll1ll_opy_ (u"࠭ࡅࡓࡔࡢࡅࡉࡊࡒࡆࡕࡖࡣࡎࡔࡖࡂࡎࡌࡈࠬᨿ"),
  bstack11ll1ll_opy_ (u"ࠧࡆࡔࡕࡣࡆࡊࡄࡓࡇࡖࡗࡤ࡛ࡎࡓࡇࡄࡇࡍࡇࡂࡍࡇࠪᩀ"),
  bstack11ll1ll_opy_ (u"ࠨࡇࡕࡖࡤ࡚ࡕࡏࡐࡈࡐࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡉࡅࡎࡒࡅࡅࠩᩁ"),
  bstack11ll1ll_opy_ (u"ࠩࡈࡖࡗࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡘࡎࡓࡅࡅࡡࡒ࡙࡙࠭ᩂ"),
  bstack11ll1ll_opy_ (u"ࠪࡉࡗࡘ࡟ࡔࡑࡆࡏࡘࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡊࡆࡏࡌࡆࡆࠪᩃ"),
  bstack11ll1ll_opy_ (u"ࠫࡊࡘࡒࡠࡕࡒࡇࡐ࡙࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣࡍࡕࡓࡕࡡࡘࡒࡗࡋࡁࡄࡊࡄࡆࡑࡋࠧᩄ"),
  bstack11ll1ll_opy_ (u"ࠬࡋࡒࡓࡡࡓࡖࡔ࡞࡙ࡠࡅࡒࡒࡓࡋࡃࡕࡋࡒࡒࡤࡌࡁࡊࡎࡈࡈࠬᩅ"),
  bstack11ll1ll_opy_ (u"࠭ࡅࡓࡔࡢࡒࡆࡓࡅࡠࡐࡒࡘࡤࡘࡅࡔࡑࡏ࡚ࡊࡊࠧᩆ"),
  bstack11ll1ll_opy_ (u"ࠧࡆࡔࡕࡣࡓࡇࡍࡆࡡࡕࡉࡘࡕࡌࡖࡖࡌࡓࡓࡥࡆࡂࡋࡏࡉࡉ࠭ᩇ"),
  bstack11ll1ll_opy_ (u"ࠨࡇࡕࡖࡤࡓࡁࡏࡆࡄࡘࡔࡘ࡙ࡠࡒࡕࡓ࡝࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟ࡇࡃࡌࡐࡊࡊࠧᩈ"),
]
bstack1l1l11111l_opy_ = bstack11ll1ll_opy_ (u"ࠩ࠱࠳ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡥࡷࡺࡩࡧࡣࡦࡸࡸ࠵ࠧᩉ")
bstack1l1l111l1_opy_ = os.path.join(os.path.expanduser(bstack11ll1ll_opy_ (u"ࠪࢂࠬᩊ")), bstack11ll1ll_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᩋ"), bstack11ll1ll_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫᩌ"))
bstack11l11lll11l_opy_ = bstack11ll1ll_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡥࡵ࡯ࠧᩍ")
bstack11l11ll1l11_opy_ = [ bstack11ll1ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧᩎ"), bstack11ll1ll_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧᩏ"), bstack11ll1ll_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨᩐ"), bstack11ll1ll_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪᩑ")]
bstack1ll1l111ll_opy_ = [ bstack11ll1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᩒ"), bstack11ll1ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫᩓ"), bstack11ll1ll_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬᩔ"), bstack11ll1ll_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧᩕ") ]
bstack1111l1ll11_opy_ = [ bstack11ll1ll_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧᩖ") ]
bstack11l11l1l11l_opy_ = [ bstack11ll1ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩᩗ") ]
bstack11l111111l_opy_ = 360
bstack11ll11l111l_opy_ = bstack11ll1ll_opy_ (u"ࠥࡥࡵࡶ࠭ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠥᩘ")
bstack11l11l1l1l1_opy_ = bstack11ll1ll_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡡࡱ࡫࠲ࡺ࠶࠵ࡩࡴࡵࡸࡩࡸࠨᩙ")
bstack11l1l111l11_opy_ = bstack11ll1ll_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫࠯ࡢࡲ࡬࠳ࡻ࠷࠯ࡪࡵࡶࡹࡪࡹ࠭ࡴࡷࡰࡱࡦࡸࡹࠣᩚ")
bstack11l1l111lll_opy_ = bstack11ll1ll_opy_ (u"ࠨࡁࡱࡲࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡵࡧࡶࡸࡸࠦࡡࡳࡧࠣࡷࡺࡶࡰࡰࡴࡷࡩࡩࠦ࡯࡯ࠢࡒࡗࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࠥࡴࠢࡤࡲࡩࠦࡡࡣࡱࡹࡩࠥ࡬࡯ࡳࠢࡄࡲࡩࡸ࡯ࡪࡦࠣࡨࡪࡼࡩࡤࡧࡶ࠲ࠧᩛ")
bstack11l11l11l1l_opy_ = bstack11ll1ll_opy_ (u"ࠢ࠲࠳࠱࠴ࠧᩜ")
bstack11lll1l1_opy_ = {
  bstack11ll1ll_opy_ (u"ࠨࡒࡄࡗࡘ࠭ᩝ"): bstack11ll1ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᩞ"),
  bstack11ll1ll_opy_ (u"ࠪࡊࡆࡏࡌࠨ᩟"): bstack11ll1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧ᩠ࠫ"),
  bstack11ll1ll_opy_ (u"࡙ࠬࡋࡊࡒࠪᩡ"): bstack11ll1ll_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᩢ")
}
bstack111lllll11_opy_ = [
  bstack11ll1ll_opy_ (u"ࠢࡨࡧࡷࠦᩣ"),
  bstack11ll1ll_opy_ (u"ࠣࡩࡲࡆࡦࡩ࡫ࠣᩤ"),
  bstack11ll1ll_opy_ (u"ࠤࡪࡳࡋࡵࡲࡸࡣࡵࡨࠧᩥ"),
  bstack11ll1ll_opy_ (u"ࠥࡶࡪ࡬ࡲࡦࡵ࡫ࠦᩦ"),
  bstack11ll1ll_opy_ (u"ࠦࡨࡲࡩࡤ࡭ࡈࡰࡪࡳࡥ࡯ࡶࠥᩧ"),
  bstack11ll1ll_opy_ (u"ࠧࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠤᩨ"),
  bstack11ll1ll_opy_ (u"ࠨࡳࡶࡤࡰ࡭ࡹࡋ࡬ࡦ࡯ࡨࡲࡹࠨᩩ"),
  bstack11ll1ll_opy_ (u"ࠢࡴࡧࡱࡨࡐ࡫ࡹࡴࡖࡲࡉࡱ࡫࡭ࡦࡰࡷࠦᩪ"),
  bstack11ll1ll_opy_ (u"ࠣࡵࡨࡲࡩࡑࡥࡺࡵࡗࡳࡆࡩࡴࡪࡸࡨࡉࡱ࡫࡭ࡦࡰࡷࠦᩫ"),
  bstack11ll1ll_opy_ (u"ࠤࡦࡰࡪࡧࡲࡆ࡮ࡨࡱࡪࡴࡴࠣᩬ"),
  bstack11ll1ll_opy_ (u"ࠥࡥࡨࡺࡩࡰࡰࡶࠦᩭ"),
  bstack11ll1ll_opy_ (u"ࠦࡪࡾࡥࡤࡷࡷࡩࡘࡩࡲࡪࡲࡷࠦᩮ"),
  bstack11ll1ll_opy_ (u"ࠧ࡫ࡸࡦࡥࡸࡸࡪࡇࡳࡺࡰࡦࡗࡨࡸࡩࡱࡶࠥᩯ"),
  bstack11ll1ll_opy_ (u"ࠨࡣ࡭ࡱࡶࡩࠧᩰ"),
  bstack11ll1ll_opy_ (u"ࠢࡲࡷ࡬ࡸࠧᩱ"),
  bstack11ll1ll_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡖࡲࡹࡨ࡮ࡁࡤࡶ࡬ࡳࡳࠨᩲ"),
  bstack11ll1ll_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡐࡹࡱࡺࡩࡕࡱࡸࡧ࡭ࠨᩳ"),
  bstack11ll1ll_opy_ (u"ࠥࡷ࡭ࡧ࡫ࡦࠤᩴ"),
  bstack11ll1ll_opy_ (u"ࠦࡨࡲ࡯ࡴࡧࡄࡴࡵࠨ᩵")
]
bstack11l11l11ll1_opy_ = [
  bstack11ll1ll_opy_ (u"ࠧࡩ࡬ࡪࡥ࡮ࠦ᩶"),
  bstack11ll1ll_opy_ (u"ࠨࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠥ᩷"),
  bstack11ll1ll_opy_ (u"ࠢࡢࡷࡷࡳࠧ᩸"),
  bstack11ll1ll_opy_ (u"ࠣ࡯ࡤࡲࡺࡧ࡬ࠣ᩹"),
  bstack11ll1ll_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦ᩺")
]
bstack1111lll1ll_opy_ = {
  bstack11ll1ll_opy_ (u"ࠥࡧࡱ࡯ࡣ࡬ࠤ᩻"): [bstack11ll1ll_opy_ (u"ࠦࡨࡲࡩࡤ࡭ࡈࡰࡪࡳࡥ࡯ࡶࠥ᩼")],
  bstack11ll1ll_opy_ (u"ࠧࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠤ᩽"): [bstack11ll1ll_opy_ (u"ࠨࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠥ᩾")],
  bstack11ll1ll_opy_ (u"ࠢࡢࡷࡷࡳ᩿ࠧ"): [bstack11ll1ll_opy_ (u"ࠣࡵࡨࡲࡩࡑࡥࡺࡵࡗࡳࡊࡲࡥ࡮ࡧࡱࡸࠧ᪀"), bstack11ll1ll_opy_ (u"ࠤࡶࡩࡳࡪࡋࡦࡻࡶࡘࡴࡇࡣࡵ࡫ࡹࡩࡊࡲࡥ࡮ࡧࡱࡸࠧ᪁"), bstack11ll1ll_opy_ (u"ࠥࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠢ᪂"), bstack11ll1ll_opy_ (u"ࠦࡨࡲࡩࡤ࡭ࡈࡰࡪࡳࡥ࡯ࡶࠥ᪃")],
  bstack11ll1ll_opy_ (u"ࠧࡳࡡ࡯ࡷࡤࡰࠧ᪄"): [bstack11ll1ll_opy_ (u"ࠨ࡭ࡢࡰࡸࡥࡱࠨ᪅")],
  bstack11ll1ll_opy_ (u"ࠢࡵࡧࡶࡸࡨࡧࡳࡦࠤ᪆"): [bstack11ll1ll_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥ᪇")],
}
bstack11l11ll1l1l_opy_ = {
  bstack11ll1ll_opy_ (u"ࠤࡦࡰ࡮ࡩ࡫ࡆ࡮ࡨࡱࡪࡴࡴࠣ᪈"): bstack11ll1ll_opy_ (u"ࠥࡧࡱ࡯ࡣ࡬ࠤ᪉"),
  bstack11ll1ll_opy_ (u"ࠦࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣ᪊"): bstack11ll1ll_opy_ (u"ࠧࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠤ᪋"),
  bstack11ll1ll_opy_ (u"ࠨࡳࡦࡰࡧࡏࡪࡿࡳࡕࡱࡈࡰࡪࡳࡥ࡯ࡶࠥ᪌"): bstack11ll1ll_opy_ (u"ࠢࡴࡧࡱࡨࡐ࡫ࡹࡴࠤ᪍"),
  bstack11ll1ll_opy_ (u"ࠣࡵࡨࡲࡩࡑࡥࡺࡵࡗࡳࡆࡩࡴࡪࡸࡨࡉࡱ࡫࡭ࡦࡰࡷࠦ᪎"): bstack11ll1ll_opy_ (u"ࠤࡶࡩࡳࡪࡋࡦࡻࡶࠦ᪏"),
  bstack11ll1ll_opy_ (u"ࠥࡸࡪࡹࡴࡤࡣࡶࡩࠧ᪐"): bstack11ll1ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡥࡤࡷࡪࠨ᪑")
}
bstack1l11ll1l_opy_ = {
  bstack11ll1ll_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩ᪒"): bstack11ll1ll_opy_ (u"࠭ࡓࡶ࡫ࡷࡩ࡙ࠥࡥࡵࡷࡳࠫ᪓"),
  bstack11ll1ll_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡁࡍࡎࠪ᪔"): bstack11ll1ll_opy_ (u"ࠨࡕࡸ࡭ࡹ࡫ࠠࡕࡧࡤࡶࡩࡵࡷ࡯ࠩ᪕"),
  bstack11ll1ll_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧ᪖"): bstack11ll1ll_opy_ (u"ࠪࡘࡪࡹࡴࠡࡕࡨࡸࡺࡶࠧ᪗"),
  bstack11ll1ll_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠨ᪘"): bstack11ll1ll_opy_ (u"࡚ࠬࡥࡴࡶࠣࡘࡪࡧࡲࡥࡱࡺࡲࠬ᪙")
}
bstack11l11llll1l_opy_ = 65536
bstack11l1l11111l_opy_ = bstack11ll1ll_opy_ (u"࠭࠮࠯࠰࡞ࡘࡗ࡛ࡎࡄࡃࡗࡉࡉࡣࠧ᪚")
bstack11l11ll111l_opy_ = [
      bstack11ll1ll_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ᪛"), bstack11ll1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ᪜"), bstack11ll1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬ᪝"), bstack11ll1ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧ᪞"), bstack11ll1ll_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸ࠭᪟"),
      bstack11ll1ll_opy_ (u"ࠬࡶࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨ᪠"), bstack11ll1ll_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡧࡳࡴࠩ᪡"), bstack11ll1ll_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡖࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨ᪢"), bstack11ll1ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡐࡳࡱࡻࡽࡕࡧࡳࡴࠩ᪣"),
      bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ᪤"), bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ᪥"), bstack11ll1ll_opy_ (u"ࠫࡦࡻࡴࡩࡖࡲ࡯ࡪࡴࠧ᪦")
    ]
bstack11l1l11l1ll_opy_= {
  bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩᪧ"): bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ᪨"),
  bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ᪩"): bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ᪪"),
  bstack11ll1ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ᪫"): bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ᪬"),
  bstack11ll1ll_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ᪭"): bstack11ll1ll_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ᪮"),
  bstack11ll1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ᪯"): bstack11ll1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ᪰"),
  bstack11ll1ll_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪ᪱"): bstack11ll1ll_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫ᪲"),
  bstack11ll1ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭᪳"): bstack11ll1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧ᪴"),
  bstack11ll1ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺ᪵ࠩ"): bstack11ll1ll_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻ᪶ࠪ"),
  bstack11ll1ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭᪷ࠪ"): bstack11ll1ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮᪸ࠫ"),
  bstack11ll1ll_opy_ (u"ࠩࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹ᪹ࠧ"): bstack11ll1ll_opy_ (u"ࠪࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠨ᪺"),
  bstack11ll1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ᪻"): bstack11ll1ll_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ᪼"),
  bstack11ll1ll_opy_ (u"࠭ࡴࡦࡵࡷࡖࡪࡶ࡯ࡳࡶ࡬ࡲ࡬᪽࠭"): bstack11ll1ll_opy_ (u"ࠧࡵࡧࡶࡸࡗ࡫ࡰࡰࡴࡷ࡭ࡳ࡭ࠧ᪾"),
  bstack11ll1ll_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷᪿࠬ"): bstack11ll1ll_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸᫀ࠭"),
  bstack11ll1ll_opy_ (u"ࠪࡸࡪࡹࡴࡓࡧࡳࡳࡷࡺࡩ࡯ࡩࡒࡴࡹ࡯࡯࡯ࡵࠪ᫁"): bstack11ll1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡔࡨࡴࡴࡸࡴࡪࡰࡪࡓࡵࡺࡩࡰࡰࡶࠫ᫂"),
  bstack11ll1ll_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱ࡛ࡧࡲࡪࡣࡥࡰࡪࡹ᫃ࠧ"): bstack11ll1ll_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠨ᫄"),
  bstack11ll1ll_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ᫅"): bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪ᫆"),
  bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ᫇"): bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ᫈"),
  bstack11ll1ll_opy_ (u"ࠫࡷ࡫ࡲࡶࡰࡗࡩࡸࡺࡳࠨ᫉"): bstack11ll1ll_opy_ (u"ࠬࡸࡥࡳࡷࡱࡘࡪࡹࡴࡴ᫊ࠩ"),
  bstack11ll1ll_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ᫋"): bstack11ll1ll_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ᫌ"),
  bstack11ll1ll_opy_ (u"ࠨࡲࡨࡶࡨࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᫍ"): bstack11ll1ll_opy_ (u"ࠩࡳࡩࡷࡩࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᫎ"),
  bstack11ll1ll_opy_ (u"ࠪࡴࡪࡸࡣࡺࡅࡤࡴࡹࡻࡲࡦࡏࡲࡨࡪ࠭᫏"): bstack11ll1ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡆࡥࡵࡺࡵࡳࡧࡐࡳࡩ࡫ࠧ᫐"),
  bstack11ll1ll_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡇࡵࡵࡱࡆࡥࡵࡺࡵࡳࡧࡏࡳ࡬ࡹࠧ᫑"): bstack11ll1ll_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁࡶࡶࡲࡇࡦࡶࡴࡶࡴࡨࡐࡴ࡭ࡳࠨ᫒"),
  bstack11ll1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ᫓"): bstack11ll1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ᫔"),
  bstack11ll1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᫕"): bstack11ll1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ᫖"),
  bstack11ll1ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ᫗"): bstack11ll1ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ᫘"),
  bstack11ll1ll_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ᫙"): bstack11ll1ll_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࡓࡵࡺࡩࡰࡰࡶࠫ᫚"),
  bstack11ll1ll_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡔࡶࡴࡪࡱࡱࡷࠬ᫛"): bstack11ll1ll_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭᫜"),
  bstack11ll1ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡕࡨࡸࡹ࡯࡮ࡨࡵࠪ᫝"): bstack11ll1ll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡖࡩࡹࡺࡩ࡯ࡩࡶࠫ᫞")
}
bstack11l1l1111l1_opy_ = [bstack11ll1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ᫟"), bstack11ll1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ᫠")]
bstack11l11111l1_opy_ = (bstack11ll1ll_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢ᫡"),)
bstack11l11ll1ll1_opy_ = bstack11ll1ll_opy_ (u"ࠨࡵࡧ࡯࠴ࡼ࠱࠰ࡷࡳࡨࡦࡺࡥࡠࡥ࡯࡭ࠬ᫢")
bstack111111111_opy_ = bstack11ll1ll_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡵ࡯࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠲ࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦ࠱ࡹ࠵࠴࡭ࡲࡪࡦࡶ࠳ࠧ᫣")
bstack111l111ll1_opy_ = bstack11ll1ll_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳࡬ࡸࡩࡥ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡪࡡࡴࡪࡥࡳࡦࡸࡤ࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࠤ᫤")
bstack1111l1111l_opy_ = bstack11ll1ll_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡧࡵࡵࡱࡰࡥࡹ࡫࠭ࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨ࠳ࡻ࠷࠯ࡣࡷ࡬ࡰࡩࡹ࠮࡫ࡵࡲࡲࠧ᫥")
class EVENTS(Enum):
  bstack11l11lll111_opy_ = bstack11ll1ll_opy_ (u"ࠬࡹࡤ࡬࠼ࡲ࠵࠶ࡿ࠺ࡱࡴ࡬ࡲࡹ࠳ࡢࡶ࡫࡯ࡨࡱ࡯࡮࡬ࠩ᫦")
  bstack1l1l1l1ll1_opy_ = bstack11ll1ll_opy_ (u"࠭ࡳࡥ࡭࠽ࡧࡱ࡫ࡡ࡯ࡷࡳࠫ᫧") # final bstack11l11ll1lll_opy_
  bstack11l11l1llll_opy_ = bstack11ll1ll_opy_ (u"ࠧࡴࡦ࡮࠾ࡸ࡫࡮ࡥ࡮ࡲ࡫ࡸ࠭᫨")
  bstack11ll111ll1_opy_ = bstack11ll1ll_opy_ (u"ࠨࡵࡧ࡯࠿ࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦ࠼ࡳࡶ࡮ࡴࡴ࠮ࡤࡸ࡭ࡱࡪ࡬ࡪࡰ࡮ࠫ᫩") #shift post bstack11l11l111l1_opy_
  bstack111ll1ll11_opy_ = bstack11ll1ll_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡥ࠻ࡲࡵ࡭ࡳࡺ࠭ࡣࡷ࡬ࡰࡩࡲࡩ࡯࡭ࠪ᫪") #shift post bstack11l11l111l1_opy_
  bstack11l11ll11l1_opy_ = bstack11ll1ll_opy_ (u"ࠪࡷࡩࡱ࠺ࡵࡧࡶࡸ࡭ࡻࡢࠨ᫫") #shift
  bstack11l11l1l111_opy_ = bstack11ll1ll_opy_ (u"ࠫࡸࡪ࡫࠻ࡲࡨࡶࡨࡿ࠺ࡥࡱࡺࡲࡱࡵࡡࡥࠩ᫬") #shift
  bstack111ll1llll_opy_ = bstack11ll1ll_opy_ (u"ࠬࡹࡤ࡬࠼ࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪࡀࡨࡶࡤ࠰ࡱࡦࡴࡡࡨࡧࡰࡩࡳࡺࠧ᫭")
  bstack1l111l1l1ll_opy_ = bstack11ll1ll_opy_ (u"࠭ࡳࡥ࡭࠽ࡥ࠶࠷ࡹ࠻ࡵࡤࡺࡪ࠳ࡲࡦࡵࡸࡰࡹࡹࠧ᫮")
  bstack111l1l1l11_opy_ = bstack11ll1ll_opy_ (u"ࠧࡴࡦ࡮࠾ࡦ࠷࠱ࡺ࠼ࡧࡶ࡮ࡼࡥࡳ࠯ࡳࡩࡷ࡬࡯ࡳ࡯ࡶࡧࡦࡴࠧ᫯")
  bstack1l111l11l1_opy_ = bstack11ll1ll_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡵࡵࡱࡰࡥࡹ࡫࠺࡭ࡱࡦࡥࡱ࠭᫰") #shift
  bstack11l11lll1_opy_ = bstack11ll1ll_opy_ (u"ࠩࡶࡨࡰࡀࡡࡱࡲ࠰ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠿ࡧࡰࡱ࠯ࡸࡴࡱࡵࡡࡥࠩ᫱") #shift
  bstack111ll11111_opy_ = bstack11ll1ll_opy_ (u"ࠪࡷࡩࡱ࠺ࡢࡷࡷࡳࡲࡧࡴࡦ࠼ࡦ࡭࠲ࡧࡲࡵ࡫ࡩࡥࡨࡺࡳࠨ᫲")
  bstack1l1l111lll_opy_ = bstack11ll1ll_opy_ (u"ࠫࡸࡪ࡫࠻ࡣ࠴࠵ࡾࡀࡧࡦࡶ࠰ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻ࠰ࡶࡪࡹࡵ࡭ࡶࡶ࠱ࡸࡻ࡭࡮ࡣࡵࡽࠬ᫳") #shift
  bstack1111111l1l_opy_ = bstack11ll1ll_opy_ (u"ࠬࡹࡤ࡬࠼ࡤ࠵࠶ࡿ࠺ࡨࡧࡷ࠱ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼ࠱ࡷ࡫ࡳࡶ࡮ࡷࡷࠬ᫴") #shift
  bstack11l1l11l1l1_opy_ = bstack11ll1ll_opy_ (u"࠭ࡳࡥ࡭࠽ࡴࡪࡸࡣࡺࠩ᫵") #shift
  bstack11llll1l111_opy_ = bstack11ll1ll_opy_ (u"ࠧࡴࡦ࡮࠾ࡵ࡫ࡲࡤࡻ࠽ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠧ᫶")
  bstack11l1l1l1ll_opy_ = bstack11ll1ll_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡵࡵࡱࡰࡥࡹ࡫࠺ࡴࡧࡶࡷ࡮ࡵ࡮࠮ࡵࡷࡥࡹࡻࡳࠨ᫷") #shift
  bstack11ll111111_opy_ = bstack11ll1ll_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡥ࠻ࡪࡸࡦ࠲ࡳࡡ࡯ࡣࡪࡩࡲ࡫࡮ࡵࠩ᫸")
  bstack11l11ll11ll_opy_ = bstack11ll1ll_opy_ (u"ࠪࡷࡩࡱ࠺ࡱࡴࡲࡼࡾ࠳ࡳࡦࡶࡸࡴࠬ᫹") #shift
  bstack11l1lll111_opy_ = bstack11ll1ll_opy_ (u"ࠫࡸࡪ࡫࠻ࡵࡨࡸࡺࡶࠧ᫺")
  bstack11l11l11l11_opy_ = bstack11ll1ll_opy_ (u"ࠬࡹࡤ࡬࠼ࡳࡩࡷࡩࡹ࠻ࡵࡱࡥࡵࡹࡨࡰࡶࠪ᫻") # not bstack11l11ll1111_opy_ in python
  bstack11l11l11l_opy_ = bstack11ll1ll_opy_ (u"࠭ࡳࡥ࡭࠽ࡨࡷ࡯ࡶࡦࡴ࠽ࡵࡺ࡯ࡴࠨ᫼") # used in bstack11l11l11lll_opy_
  bstack1l1l11lll1_opy_ = bstack11ll1ll_opy_ (u"ࠧࡴࡦ࡮࠾ࡩࡸࡩࡷࡧࡵ࠾࡬࡫ࡴࠨ᫽") # used in bstack11l11l11lll_opy_
  bstack11lll1l1ll_opy_ = bstack11ll1ll_opy_ (u"ࠨࡵࡧ࡯࠿࡮࡯ࡰ࡭ࠪ᫾")
  bstack11ll11l1l_opy_ = bstack11ll1ll_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡥ࠻ࡵࡨࡷࡸ࡯࡯࡯࠯ࡱࡥࡲ࡫ࠧ᫿")
  bstack111l1l11l_opy_ = bstack11ll1ll_opy_ (u"ࠪࡷࡩࡱ࠺ࡢࡷࡷࡳࡲࡧࡴࡦ࠼ࡶࡩࡸࡹࡩࡰࡰ࠰ࡥࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠧᬀ") #
  bstack11l11l1lll_opy_ = bstack11ll1ll_opy_ (u"ࠫࡸࡪ࡫࠻ࡱ࠴࠵ࡾࡀࡤࡳ࡫ࡹࡩࡷ࠳ࡴࡢ࡭ࡨࡗࡨࡸࡥࡦࡰࡖ࡬ࡴࡺࠧᬁ")
  bstack1111ll1ll_opy_ = bstack11ll1ll_opy_ (u"ࠬࡹࡤ࡬࠼ࡳࡩࡷࡩࡹ࠻ࡣࡸࡸࡴ࠳ࡣࡢࡲࡷࡹࡷ࡫ࠧᬂ")
  bstack11lllll1l_opy_ = bstack11ll1ll_opy_ (u"࠭ࡳࡥ࡭࠽ࡴࡷ࡫࠭ࡵࡧࡶࡸࠬᬃ")
  bstack11l1llll1l_opy_ = bstack11ll1ll_opy_ (u"ࠧࡴࡦ࡮࠾ࡵࡵࡳࡵ࠯ࡷࡩࡸࡺࠧᬄ")
  bstack11l11ll11_opy_ = bstack11ll1ll_opy_ (u"ࠨࡵࡧ࡯࠿ࡪࡲࡪࡸࡨࡶ࠿ࡶࡲࡦ࠯࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡦࡺࡩࡰࡰࠪᬅ") #shift
  bstack1l1l11l11l_opy_ = bstack11ll1ll_opy_ (u"ࠩࡶࡨࡰࡀࡤࡳ࡫ࡹࡩࡷࡀࡰࡰࡵࡷ࠱࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࢀࡡࡵ࡫ࡲࡲࠬᬆ") #shift
  bstack11l11l1ll1l_opy_ = bstack11ll1ll_opy_ (u"ࠪࡷࡩࡱ࠺ࡢࡷࡷࡳ࠲ࡩࡡࡱࡶࡸࡶࡪ࠭ᬇ")
  bstack11l11l111ll_opy_ = bstack11ll1ll_opy_ (u"ࠫࡸࡪ࡫࠻ࡣࡸࡸࡴࡳࡡࡵࡧ࠽࡭ࡩࡲࡥ࠮ࡶ࡬ࡱࡪࡵࡵࡵࠩᬈ")
  bstack1l1l1ll11ll_opy_ = bstack11ll1ll_opy_ (u"ࠬࡹࡤ࡬࠼ࡦࡰ࡮ࡀࡳࡵࡣࡵࡸࠬᬉ")
  bstack11l11l1lll1_opy_ = bstack11ll1ll_opy_ (u"࠭ࡳࡥ࡭࠽ࡧࡱ࡯࠺ࡥࡱࡺࡲࡱࡵࡡࡥࠩᬊ")
  bstack11l1l111l1l_opy_ = bstack11ll1ll_opy_ (u"ࠧࡴࡦ࡮࠾ࡨࡲࡩ࠻ࡥ࡫ࡩࡨࡱ࠭ࡶࡲࡧࡥࡹ࡫ࠧᬋ")
  bstack1l1l111111l_opy_ = bstack11ll1ll_opy_ (u"ࠨࡵࡧ࡯࠿ࡩ࡬ࡪ࠼ࡲࡲ࠲ࡨ࡯ࡰࡶࡶࡸࡷࡧࡰࠨᬌ")
  bstack1l11lll11l1_opy_ = bstack11ll1ll_opy_ (u"ࠩࡶࡨࡰࡀࡣ࡭࡫࠽ࡳࡳ࠳ࡣࡰࡰࡱࡩࡨࡺࠧᬍ")
  bstack1l1l11l1l1l_opy_ = bstack11ll1ll_opy_ (u"ࠪࡷࡩࡱ࠺ࡤ࡮࡬࠾ࡴࡴ࠭ࡴࡶࡲࡴࠬᬎ")
  bstack1l1l11111ll_opy_ = bstack11ll1ll_opy_ (u"ࠫࡸࡪ࡫࠻ࡵࡷࡥࡷࡺࡂࡪࡰࡖࡩࡸࡹࡩࡰࡰࠪᬏ")
  bstack1l1l1l1lll1_opy_ = bstack11ll1ll_opy_ (u"ࠬࡹࡤ࡬࠼ࡦࡳࡳࡴࡥࡤࡶࡅ࡭ࡳ࡙ࡥࡴࡵ࡬ࡳࡳ࠭ᬐ")
  bstack11l1l1111ll_opy_ = bstack11ll1ll_opy_ (u"࠭ࡳࡥ࡭࠽ࡨࡷ࡯ࡶࡦࡴࡌࡲ࡮ࡺࠧᬑ")
  bstack11l11l1ll11_opy_ = bstack11ll1ll_opy_ (u"ࠧࡴࡦ࡮࠾࡫࡯࡮ࡥࡐࡨࡥࡷ࡫ࡳࡵࡊࡸࡦࠬᬒ")
  bstack1lllll11l11_opy_ = bstack11ll1ll_opy_ (u"ࠨࡵࡧ࡯࠿ࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡍࡳ࡯ࡴࠨᬓ")
  bstack1llll1l1l1l_opy_ = bstack11ll1ll_opy_ (u"ࠩࡶࡨࡰࡀࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࡘࡺࡡࡳࡶࠪᬔ")
  bstack1l111l1l1l1_opy_ = bstack11ll1ll_opy_ (u"ࠪࡷࡩࡱ࠺ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡃࡰࡰࡩ࡭࡬࠭ᬕ")
  bstack11l11lllll1_opy_ = bstack11ll1ll_opy_ (u"ࠫࡸࡪ࡫࠻ࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࡄࡱࡱࡪ࡮࡭ࠧᬖ")
  bstack1l1ll11l1l1_opy_ = bstack11ll1ll_opy_ (u"ࠬࡹࡤ࡬࠼ࡤ࡭ࡘ࡫࡬ࡧࡊࡨࡥࡱ࡙ࡴࡦࡲࠪᬗ")
  bstack1l1ll11l111_opy_ = bstack11ll1ll_opy_ (u"࠭ࡳࡥ࡭࠽ࡥ࡮࡙ࡥ࡭ࡨࡋࡩࡦࡲࡇࡦࡶࡕࡩࡸࡻ࡬ࡵࠩᬘ")
  bstack1l11l1l1111_opy_ = bstack11ll1ll_opy_ (u"ࠧࡴࡦ࡮࠾ࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡉࡻ࡫࡮ࡵࠩᬙ")
  bstack1l111lll111_opy_ = bstack11ll1ll_opy_ (u"ࠨࡵࡧ࡯࠿ࡺࡥࡴࡶࡖࡩࡸࡹࡩࡰࡰࡈࡺࡪࡴࡴࠨᬚ")
  bstack1l111lllll1_opy_ = bstack11ll1ll_opy_ (u"ࠩࡶࡨࡰࡀࡣ࡭࡫࠽ࡰࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࡅࡷࡧࡱࡸࠬᬛ")
  bstack11l11l1111l_opy_ = bstack11ll1ll_opy_ (u"ࠪࡷࡩࡱ࠺ࡤ࡮࡬࠾ࡪࡴࡱࡶࡧࡸࡩ࡙࡫ࡳࡵࡇࡹࡩࡳࡺࠧᬜ")
  bstack1lllll1l1ll_opy_ = bstack11ll1ll_opy_ (u"ࠫࡸࡪ࡫࠻ࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࡓࡵࡱࡳࠫᬝ")
  bstack1l1l1111l11_opy_ = bstack11ll1ll_opy_ (u"ࠬࡹࡤ࡬࠼ࡲࡲࡘࡺ࡯ࡱࠩᬞ")
class STAGE(Enum):
  bstack1ll111111_opy_ = bstack11ll1ll_opy_ (u"࠭ࡳࡵࡣࡵࡸࠬᬟ")
  END = bstack11ll1ll_opy_ (u"ࠧࡦࡰࡧࠫᬠ")
  bstack11l11ll1ll_opy_ = bstack11ll1ll_opy_ (u"ࠨࡵ࡬ࡲ࡬ࡲࡥࠨᬡ")
bstack11l11l1l11_opy_ = {
  bstack11ll1ll_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࠩᬢ"): bstack11ll1ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪᬣ"),
  bstack11ll1ll_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗ࠱ࡇࡊࡄࠨᬤ"): bstack11ll1ll_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸ࠲ࡩࡵࡤࡷࡰࡦࡪࡸࠧᬥ")
}
PLAYWRIGHT_HUB_URL = bstack11ll1ll_opy_ (u"ࠨࡷࡴࡵ࠽࠳࠴ࡩࡤࡱ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡁࡦࡥࡵࡹ࠽ࠣᬦ")
bstack1l111ll1111_opy_ = 98
bstack1l111111lll_opy_ = 100
bstack1lllll1ll_opy_ = {
  bstack11ll1ll_opy_ (u"ࠧࡳࡧࡵࡹࡳ࠭ᬧ"): bstack11ll1ll_opy_ (u"ࠨ࠯࠰ࡶࡪࡸࡵ࡯ࡵࠪᬨ"),
  bstack11ll1ll_opy_ (u"ࠩࡧࡩࡱࡧࡹࠨᬩ"): bstack11ll1ll_opy_ (u"ࠪ࠱࠲ࡸࡥࡳࡷࡱࡷ࠲ࡪࡥ࡭ࡣࡼࠫᬪ"),
  bstack11ll1ll_opy_ (u"ࠫࡷ࡫ࡲࡶࡰ࠰ࡨࡪࡲࡡࡺࠩᬫ"): 0
}
bstack11ll1l1llll_opy_ = bstack11ll1ll_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡣࡰ࡮࡯ࡩࡨࡺ࡯ࡳ࠯ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠧᬬ")
bstack11l11lll1l1_opy_ = bstack11ll1ll_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࡶࡲ࡯ࡳࡦࡪ࠭ࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠥᬭ")
bstack11ll1l1l1_opy_ = bstack11ll1ll_opy_ (u"ࠢࡕࡇࡖࡘࠥࡘࡅࡑࡑࡕࡘࡎࡔࡇࠡࡃࡑࡈࠥࡇࡎࡂࡎ࡜ࡘࡎࡉࡓࠣᬮ")