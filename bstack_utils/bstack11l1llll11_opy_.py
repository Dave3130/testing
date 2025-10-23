# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import os
import json
from bstack_utils.bstack11111ll111_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll1l1l1l_opy_(object):
  bstack1111l11l11_opy_ = os.path.join(os.path.expanduser(bstack111111l_opy_ (u"ࠪࢂࠬᾟ")), bstack111111l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᾠ"))
  bstack1lllll1l1l11_opy_ = os.path.join(bstack1111l11l11_opy_, bstack111111l_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹ࠮࡫ࡵࡲࡲࠬᾡ"))
  commands_to_wrap = None
  perform_scan = None
  bstack1ll111ll11_opy_ = None
  bstack11lll11lll_opy_ = None
  bstack1lllll1l111l_opy_ = None
  bstack1lllll1l1ll1_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack111111l_opy_ (u"࠭ࡩ࡯ࡵࡷࡥࡳࡩࡥࠨᾢ")):
      cls.instance = super(bstack1lllll1l1l1l_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll1l11l1_opy_()
    return cls.instance
  def bstack1lllll1l11l1_opy_(self):
    try:
      with open(self.bstack1lllll1l1l11_opy_, bstack111111l_opy_ (u"ࠧࡳࠩᾣ")) as bstack1l1ll1l111_opy_:
        bstack1lllll1l11ll_opy_ = bstack1l1ll1l111_opy_.read()
        data = json.loads(bstack1lllll1l11ll_opy_)
        if bstack111111l_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࠪᾤ") in data:
          self.bstack1lllll11llll_opy_(data[bstack111111l_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶࠫᾥ")])
        if bstack111111l_opy_ (u"ࠪࡷࡨࡸࡩࡱࡶࡶࠫᾦ") in data:
          self.bstack1l1llll11l_opy_(data[bstack111111l_opy_ (u"ࠫࡸࡩࡲࡪࡲࡷࡷࠬᾧ")])
        if bstack111111l_opy_ (u"ࠬࡴ࡯࡯ࡄࡖࡸࡦࡩ࡫ࡊࡰࡩࡶࡦࡇ࠱࠲ࡻࡆ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᾨ") in data:
          self.bstack1lllll1l1111_opy_(data[bstack111111l_opy_ (u"࠭࡮ࡰࡰࡅࡗࡹࡧࡣ࡬ࡋࡱࡪࡷࡧࡁ࠲࠳ࡼࡇ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᾩ")])
    except:
      pass
  def bstack1lllll1l1111_opy_(self, bstack1lllll1l1ll1_opy_):
    if bstack1lllll1l1ll1_opy_ != None:
      self.bstack1lllll1l1ll1_opy_ = bstack1lllll1l1ll1_opy_
  def bstack1l1llll11l_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack111111l_opy_ (u"ࠧࡴࡥࡤࡲࠬᾪ"),bstack111111l_opy_ (u"ࠨࠩᾫ"))
      self.bstack1ll111ll11_opy_ = scripts.get(bstack111111l_opy_ (u"ࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࠭ᾬ"),bstack111111l_opy_ (u"ࠪࠫᾭ"))
      self.bstack11lll11lll_opy_ = scripts.get(bstack111111l_opy_ (u"ࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠨᾮ"),bstack111111l_opy_ (u"ࠬ࠭ᾯ"))
      self.bstack1lllll1l111l_opy_ = scripts.get(bstack111111l_opy_ (u"࠭ࡳࡢࡸࡨࡖࡪࡹࡵ࡭ࡶࡶࠫᾰ"),bstack111111l_opy_ (u"ࠧࠨᾱ"))
  def bstack1lllll11llll_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll1l1l11_opy_, bstack111111l_opy_ (u"ࠨࡹࠪᾲ")) as file:
        json.dump({
          bstack111111l_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡶࠦᾳ"): self.commands_to_wrap,
          bstack111111l_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࡶࠦᾴ"): {
            bstack111111l_opy_ (u"ࠦࡸࡩࡡ࡯ࠤ᾵"): self.perform_scan,
            bstack111111l_opy_ (u"ࠧ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠤᾶ"): self.bstack1ll111ll11_opy_,
            bstack111111l_opy_ (u"ࠨࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࡖࡹࡲࡳࡡࡳࡻࠥᾷ"): self.bstack11lll11lll_opy_,
            bstack111111l_opy_ (u"ࠢࡴࡣࡹࡩࡗ࡫ࡳࡶ࡮ࡷࡷࠧᾸ"): self.bstack1lllll1l111l_opy_
          },
          bstack111111l_opy_ (u"ࠣࡰࡲࡲࡇ࡙ࡴࡢࡥ࡮ࡍࡳ࡬ࡲࡢࡃ࠴࠵ࡾࡉࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠧᾹ"): self.bstack1lllll1l1ll1_opy_
        }, file)
    except Exception as e:
      logger.error(bstack111111l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡴࡶࡲࡶ࡮ࡴࡧࠡࡥࡲࡱࡲࡧ࡮ࡥࡵ࠽ࠤࢀࢃࠢᾺ").format(e))
      pass
  def bstack1ll111lll_opy_(self, command_name):
    try:
      return any(command.get(bstack111111l_opy_ (u"ࠪࡲࡦࡳࡥࠨΆ")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack11l1llll11_opy_ = bstack1lllll1l1l1l_opy_()