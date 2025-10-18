# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import os
import json
from bstack_utils.bstack111l11l1l_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll1l1111_opy_(object):
  bstack111l1lll1l_opy_ = os.path.join(os.path.expanduser(bstack1l1lll1_opy_ (u"ࠫࢃ࠭ᾧ")), bstack1l1lll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᾨ"))
  bstack1lllll1l11ll_opy_ = os.path.join(bstack111l1lll1l_opy_, bstack1l1lll1_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳ࠯࡬ࡶࡳࡳ࠭ᾩ"))
  commands_to_wrap = None
  perform_scan = None
  bstack1ll1lll11l_opy_ = None
  bstack1ll111111_opy_ = None
  bstack1lllll1l111l_opy_ = None
  bstack1lllll11llll_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack1l1lll1_opy_ (u"ࠧࡪࡰࡶࡸࡦࡴࡣࡦࠩᾪ")):
      cls.instance = super(bstack1lllll1l1111_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll11ll1l_opy_()
    return cls.instance
  def bstack1lllll11ll1l_opy_(self):
    try:
      with open(self.bstack1lllll1l11ll_opy_, bstack1l1lll1_opy_ (u"ࠨࡴࠪᾫ")) as bstack11l1ll1ll_opy_:
        bstack1lllll1l1l11_opy_ = bstack11l1ll1ll_opy_.read()
        data = json.loads(bstack1lllll1l1l11_opy_)
        if bstack1l1lll1_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶࠫᾬ") in data:
          self.bstack1lllll1l11l1_opy_(data[bstack1l1lll1_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷࠬᾭ")])
        if bstack1l1lll1_opy_ (u"ࠫࡸࡩࡲࡪࡲࡷࡷࠬᾮ") in data:
          self.bstack11l11l1ll_opy_(data[bstack1l1lll1_opy_ (u"ࠬࡹࡣࡳ࡫ࡳࡸࡸ࠭ᾯ")])
        if bstack1l1lll1_opy_ (u"࠭࡮ࡰࡰࡅࡗࡹࡧࡣ࡬ࡋࡱࡪࡷࡧࡁ࠲࠳ࡼࡇ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᾰ") in data:
          self.bstack1lllll11lll1_opy_(data[bstack1l1lll1_opy_ (u"ࠧ࡯ࡱࡱࡆࡘࡺࡡࡤ࡭ࡌࡲ࡫ࡸࡡࡂ࠳࠴ࡽࡈ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫᾱ")])
    except:
      pass
  def bstack1lllll11lll1_opy_(self, bstack1lllll11llll_opy_):
    if bstack1lllll11llll_opy_ != None:
      self.bstack1lllll11llll_opy_ = bstack1lllll11llll_opy_
  def bstack11l11l1ll_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack1l1lll1_opy_ (u"ࠨࡵࡦࡥࡳ࠭ᾲ"),bstack1l1lll1_opy_ (u"ࠩࠪᾳ"))
      self.bstack1ll1lll11l_opy_ = scripts.get(bstack1l1lll1_opy_ (u"ࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠧᾴ"),bstack1l1lll1_opy_ (u"ࠫࠬ᾵"))
      self.bstack1ll111111_opy_ = scripts.get(bstack1l1lll1_opy_ (u"ࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࡕࡸࡱࡲࡧࡲࡺࠩᾶ"),bstack1l1lll1_opy_ (u"࠭ࠧᾷ"))
      self.bstack1lllll1l111l_opy_ = scripts.get(bstack1l1lll1_opy_ (u"ࠧࡴࡣࡹࡩࡗ࡫ࡳࡶ࡮ࡷࡷࠬᾸ"),bstack1l1lll1_opy_ (u"ࠨࠩᾹ"))
  def bstack1lllll1l11l1_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll1l11ll_opy_, bstack1l1lll1_opy_ (u"ࠩࡺࠫᾺ")) as file:
        json.dump({
          bstack1l1lll1_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡷࠧΆ"): self.commands_to_wrap,
          bstack1l1lll1_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࡷࠧᾼ"): {
            bstack1l1lll1_opy_ (u"ࠧࡹࡣࡢࡰࠥ᾽"): self.perform_scan,
            bstack1l1lll1_opy_ (u"ࠨࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠥι"): self.bstack1ll1lll11l_opy_,
            bstack1l1lll1_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼࠦ᾿"): self.bstack1ll111111_opy_,
            bstack1l1lll1_opy_ (u"ࠣࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸࠨ῀"): self.bstack1lllll1l111l_opy_
          },
          bstack1l1lll1_opy_ (u"ࠤࡱࡳࡳࡈࡓࡵࡣࡦ࡯ࡎࡴࡦࡳࡣࡄ࠵࠶ࡿࡃࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸࠨ῁"): self.bstack1lllll11llll_opy_
        }, file)
    except Exception as e:
      logger.error(bstack1l1lll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡵࡷࡳࡷ࡯࡮ࡨࠢࡦࡳࡲࡳࡡ࡯ࡦࡶ࠾ࠥࢁࡽࠣῂ").format(e))
      pass
  def bstack111l11l1l1_opy_(self, command_name):
    try:
      return any(command.get(bstack1l1lll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩῃ")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack1l11111ll_opy_ = bstack1lllll1l1111_opy_()