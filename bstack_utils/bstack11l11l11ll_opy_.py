# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import os
import json
from bstack_utils.bstack11llll111l_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll111l1l_opy_(object):
  bstack1l11l1ll11_opy_ = os.path.join(os.path.expanduser(bstack1lllll1l_opy_ (u"ࠫࢃ࠭Ὴ")), bstack1lllll1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬΉ"))
  bstack1lllll111lll_opy_ = os.path.join(bstack1l11l1ll11_opy_, bstack1lllll1l_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳ࠯࡬ࡶࡳࡳ࠭ῌ"))
  commands_to_wrap = None
  perform_scan = None
  bstack1llll1l11l_opy_ = None
  bstack11l1l1111l_opy_ = None
  bstack1lllll111ll1_opy_ = None
  bstack1lllll11l11l_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack1lllll1l_opy_ (u"ࠧࡪࡰࡶࡸࡦࡴࡣࡦࠩ῍")):
      cls.instance = super(bstack1lllll111l1l_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll11ll11_opy_()
    return cls.instance
  def bstack1lllll11ll11_opy_(self):
    try:
      with open(self.bstack1lllll111lll_opy_, bstack1lllll1l_opy_ (u"ࠨࡴࠪ῎")) as bstack1ll11ll11_opy_:
        bstack1lllll11l1ll_opy_ = bstack1ll11ll11_opy_.read()
        data = json.loads(bstack1lllll11l1ll_opy_)
        if bstack1lllll1l_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶࠫ῏") in data:
          self.bstack1lllll11l1l1_opy_(data[bstack1lllll1l_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷࠬῐ")])
        if bstack1lllll1l_opy_ (u"ࠫࡸࡩࡲࡪࡲࡷࡷࠬῑ") in data:
          self.bstack11lll1lll_opy_(data[bstack1lllll1l_opy_ (u"ࠬࡹࡣࡳ࡫ࡳࡸࡸ࠭ῒ")])
        if bstack1lllll1l_opy_ (u"࠭࡮ࡰࡰࡅࡗࡹࡧࡣ࡬ࡋࡱࡪࡷࡧࡁ࠲࠳ࡼࡇ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪΐ") in data:
          self.bstack1lllll11l111_opy_(data[bstack1lllll1l_opy_ (u"ࠧ࡯ࡱࡱࡆࡘࡺࡡࡤ࡭ࡌࡲ࡫ࡸࡡࡂ࠳࠴ࡽࡈ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ῔")])
    except:
      pass
  def bstack1lllll11l111_opy_(self, bstack1lllll11l11l_opy_):
    if bstack1lllll11l11l_opy_ != None:
      self.bstack1lllll11l11l_opy_ = bstack1lllll11l11l_opy_
  def bstack11lll1lll_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack1lllll1l_opy_ (u"ࠨࡵࡦࡥࡳ࠭῕"),bstack1lllll1l_opy_ (u"ࠩࠪῖ"))
      self.bstack1llll1l11l_opy_ = scripts.get(bstack1lllll1l_opy_ (u"ࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠧῗ"),bstack1lllll1l_opy_ (u"ࠫࠬῘ"))
      self.bstack11l1l1111l_opy_ = scripts.get(bstack1lllll1l_opy_ (u"ࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࡕࡸࡱࡲࡧࡲࡺࠩῙ"),bstack1lllll1l_opy_ (u"࠭ࠧῚ"))
      self.bstack1lllll111ll1_opy_ = scripts.get(bstack1lllll1l_opy_ (u"ࠧࡴࡣࡹࡩࡗ࡫ࡳࡶ࡮ࡷࡷࠬΊ"),bstack1lllll1l_opy_ (u"ࠨࠩ῜"))
  def bstack1lllll11l1l1_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll111lll_opy_, bstack1lllll1l_opy_ (u"ࠩࡺࠫ῝")) as file:
        json.dump({
          bstack1lllll1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡷࠧ῞"): self.commands_to_wrap,
          bstack1lllll1l_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࡷࠧ῟"): {
            bstack1lllll1l_opy_ (u"ࠧࡹࡣࡢࡰࠥῠ"): self.perform_scan,
            bstack1lllll1l_opy_ (u"ࠨࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠥῡ"): self.bstack1llll1l11l_opy_,
            bstack1lllll1l_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼࠦῢ"): self.bstack11l1l1111l_opy_,
            bstack1lllll1l_opy_ (u"ࠣࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸࠨΰ"): self.bstack1lllll111ll1_opy_
          },
          bstack1lllll1l_opy_ (u"ࠤࡱࡳࡳࡈࡓࡵࡣࡦ࡯ࡎࡴࡦࡳࡣࡄ࠵࠶ࡿࡃࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸࠨῤ"): self.bstack1lllll11l11l_opy_
        }, file)
    except Exception as e:
      logger.error(bstack1lllll1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡵࡷࡳࡷ࡯࡮ࡨࠢࡦࡳࡲࡳࡡ࡯ࡦࡶ࠾ࠥࢁࡽࠣῥ").format(e))
      pass
  def bstack1l1lll1l1_opy_(self, command_name):
    try:
      return any(command.get(bstack1lllll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩῦ")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack11l11l11ll_opy_ = bstack1lllll111l1l_opy_()