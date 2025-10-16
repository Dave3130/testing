# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import os
import json
from bstack_utils.bstack1l1l1l1111_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll1l1lll_opy_(object):
  bstack1l1llll11_opy_ = os.path.join(os.path.expanduser(bstack1ll11_opy_ (u"࠭ࡾࠨᾩ")), bstack1ll11_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᾪ"))
  bstack1lllll1l1111_opy_ = os.path.join(bstack1l1llll11_opy_, bstack1ll11_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵ࠱࡮ࡸࡵ࡮ࠨᾫ"))
  commands_to_wrap = None
  perform_scan = None
  bstack1l111ll1l1_opy_ = None
  bstack1l11111l1l_opy_ = None
  bstack1lllll1l11ll_opy_ = None
  bstack1lllll1l1l11_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack1ll11_opy_ (u"ࠩ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠫᾬ")):
      cls.instance = super(bstack1lllll1l1lll_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll1l111l_opy_()
    return cls.instance
  def bstack1lllll1l111l_opy_(self):
    try:
      with open(self.bstack1lllll1l1111_opy_, bstack1ll11_opy_ (u"ࠪࡶࠬᾭ")) as bstack1ll1ll1ll1_opy_:
        bstack1lllll1l1ll1_opy_ = bstack1ll1ll1ll1_opy_.read()
        data = json.loads(bstack1lllll1l1ll1_opy_)
        if bstack1ll11_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭ᾮ") in data:
          self.bstack1lllll1l1l1l_opy_(data[bstack1ll11_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧᾯ")])
        if bstack1ll11_opy_ (u"࠭ࡳࡤࡴ࡬ࡴࡹࡹࠧᾰ") in data:
          self.bstack1l11l1llll_opy_(data[bstack1ll11_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨᾱ")])
        if bstack1ll11_opy_ (u"ࠨࡰࡲࡲࡇ࡙ࡴࡢࡥ࡮ࡍࡳ࡬ࡲࡢࡃ࠴࠵ࡾࡉࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬᾲ") in data:
          self.bstack1lllll1l11l1_opy_(data[bstack1ll11_opy_ (u"ࠩࡱࡳࡳࡈࡓࡵࡣࡦ࡯ࡎࡴࡦࡳࡣࡄ࠵࠶ࡿࡃࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᾳ")])
    except:
      pass
  def bstack1lllll1l11l1_opy_(self, bstack1lllll1l1l11_opy_):
    if bstack1lllll1l1l11_opy_ != None:
      self.bstack1lllll1l1l11_opy_ = bstack1lllll1l1l11_opy_
  def bstack1l11l1llll_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack1ll11_opy_ (u"ࠪࡷࡨࡧ࡮ࠨᾴ"),bstack1ll11_opy_ (u"ࠫࠬ᾵"))
      self.bstack1l111ll1l1_opy_ = scripts.get(bstack1ll11_opy_ (u"ࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠩᾶ"),bstack1ll11_opy_ (u"࠭ࠧᾷ"))
      self.bstack1l11111l1l_opy_ = scripts.get(bstack1ll11_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼࠫᾸ"),bstack1ll11_opy_ (u"ࠨࠩᾹ"))
      self.bstack1lllll1l11ll_opy_ = scripts.get(bstack1ll11_opy_ (u"ࠩࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠧᾺ"),bstack1ll11_opy_ (u"ࠪࠫΆ"))
  def bstack1lllll1l1l1l_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll1l1111_opy_, bstack1ll11_opy_ (u"ࠫࡼ࠭ᾼ")) as file:
        json.dump({
          bstack1ll11_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡹࠢ᾽"): self.commands_to_wrap,
          bstack1ll11_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࡹࠢι"): {
            bstack1ll11_opy_ (u"ࠢࡴࡥࡤࡲࠧ᾿"): self.perform_scan,
            bstack1ll11_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠧ῀"): self.bstack1l111ll1l1_opy_,
            bstack1ll11_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾࠨ῁"): self.bstack1l11111l1l_opy_,
            bstack1ll11_opy_ (u"ࠥࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠣῂ"): self.bstack1lllll1l11ll_opy_
          },
          bstack1ll11_opy_ (u"ࠦࡳࡵ࡮ࡃࡕࡷࡥࡨࡱࡉ࡯ࡨࡵࡥࡆ࠷࠱ࡺࡅ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠣῃ"): self.bstack1lllll1l1l11_opy_
        }, file)
    except Exception as e:
      logger.error(bstack1ll11_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡹࡵࡲࡪࡰࡪࠤࡨࡵ࡭࡮ࡣࡱࡨࡸࡀࠠࡼࡿࠥῄ").format(e))
      pass
  def bstack1lll1111l1_opy_(self, command_name):
    try:
      return any(command.get(bstack1ll11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ῅")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack11111lll11_opy_ = bstack1lllll1l1lll_opy_()