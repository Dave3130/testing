# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import os
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack1ll1l1l11l_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11lllll1l_opy_ import bstack1l111111l1_opy_
class bstack1ll1l11l1_opy_:
  working_dir = os.getcwd()
  bstack11llll11ll_opy_ = False
  config = {}
  bstack111l1llll11_opy_ = bstack11l11l1_opy_ (u"ࠪࠫἽ")
  binary_path = bstack11l11l1_opy_ (u"ࠫࠬἾ")
  bstack1111111l1ll_opy_ = bstack11l11l1_opy_ (u"ࠬ࠭Ἷ")
  bstack1ll111111l_opy_ = False
  bstack1lllll1lllll_opy_ = None
  bstack11111111111_opy_ = {}
  bstack1lllllll11ll_opy_ = 300
  bstack1llllll1111l_opy_ = False
  logger = None
  bstack1llllll1llll_opy_ = False
  bstack11llllll1l_opy_ = False
  percy_build_id = None
  bstack1llllll11lll_opy_ = bstack11l11l1_opy_ (u"࠭ࠧὀ")
  bstack1llllll111ll_opy_ = {
    bstack11l11l1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧὁ") : 1,
    bstack11l11l1_opy_ (u"ࠨࡨ࡬ࡶࡪ࡬࡯ࡹࠩὂ") : 2,
    bstack11l11l1_opy_ (u"ࠩࡨࡨ࡬࡫ࠧὃ") : 3,
    bstack11l11l1_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪὄ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1lllll1l1lll_opy_(self):
    bstack11111111l11_opy_ = bstack11l11l1_opy_ (u"ࠫࠬὅ")
    bstack1llllll11ll1_opy_ = sys.platform
    bstack1llllll11l11_opy_ = bstack11l11l1_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ὆")
    if re.match(bstack11l11l1_opy_ (u"ࠨࡤࡢࡴࡺ࡭ࡳࢂ࡭ࡢࡥࠣࡳࡸࠨ὇"), bstack1llllll11ll1_opy_) != None:
      bstack11111111l11_opy_ = bstack11l1l111ll1_opy_ + bstack11l11l1_opy_ (u"ࠢ࠰ࡲࡨࡶࡨࡿ࠭ࡰࡵࡻ࠲ࡿ࡯ࡰࠣὈ")
      self.bstack1llllll11lll_opy_ = bstack11l11l1_opy_ (u"ࠨ࡯ࡤࡧࠬὉ")
    elif re.match(bstack11l11l1_opy_ (u"ࠤࡰࡷࡼ࡯࡮ࡽ࡯ࡶࡽࡸࢂ࡭ࡪࡰࡪࡻࢁࡩࡹࡨࡹ࡬ࡲࢁࡨࡣࡤࡹ࡬ࡲࢁࡽࡩ࡯ࡥࡨࢀࡪࡳࡣࡽࡹ࡬ࡲ࠸࠸ࠢὊ"), bstack1llllll11ll1_opy_) != None:
      bstack11111111l11_opy_ = bstack11l1l111ll1_opy_ + bstack11l11l1_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠰ࡻ࡮ࡴ࠮ࡻ࡫ࡳࠦὋ")
      bstack1llllll11l11_opy_ = bstack11l11l1_opy_ (u"ࠦࡵ࡫ࡲࡤࡻ࠱ࡩࡽ࡫ࠢὌ")
      self.bstack1llllll11lll_opy_ = bstack11l11l1_opy_ (u"ࠬࡽࡩ࡯ࠩὍ")
    else:
      bstack11111111l11_opy_ = bstack11l1l111ll1_opy_ + bstack11l11l1_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠳࡬ࡪࡰࡸࡼ࠳ࢀࡩࡱࠤ὎")
      self.bstack1llllll11lll_opy_ = bstack11l11l1_opy_ (u"ࠧ࡭࡫ࡱࡹࡽ࠭὏")
    return bstack11111111l11_opy_, bstack1llllll11l11_opy_
  def bstack11111111ll1_opy_(self):
    try:
      bstack1lllll11llll_opy_ = [os.path.join(expanduser(bstack11l11l1_opy_ (u"ࠣࢀࠥὐ")), bstack11l11l1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩὑ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1lllll11llll_opy_:
        if(self.bstack1llllll1ll1l_opy_(path)):
          return path
      raise bstack11l11l1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠢὒ")
    except Exception as e:
      self.logger.error(bstack11l11l1_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥࠡࡲࡤࡸ࡭ࠦࡦࡰࡴࠣࡴࡪࡸࡣࡺࠢࡧࡳࡼࡴ࡬ࡰࡣࡧ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࠯ࠣࡿࢂࠨὓ").format(e))
  def bstack1llllll1ll1l_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1lllll1l1l11_opy_(self, bstack1111111l111_opy_):
    return os.path.join(bstack1111111l111_opy_, self.bstack111l1llll11_opy_ + bstack11l11l1_opy_ (u"ࠧ࠴ࡥࡵࡣࡪࠦὔ"))
  def bstack1llllll1lll1_opy_(self, bstack1111111l111_opy_, bstack1llllllll1ll_opy_):
    if not bstack1llllllll1ll_opy_: return
    try:
      bstack11111111l1l_opy_ = self.bstack1lllll1l1l11_opy_(bstack1111111l111_opy_)
      with open(bstack11111111l1l_opy_, bstack11l11l1_opy_ (u"ࠨࡷࠣὕ")) as f:
        f.write(bstack1llllllll1ll_opy_)
        self.logger.debug(bstack11l11l1_opy_ (u"ࠢࡔࡣࡹࡩࡩࠦ࡮ࡦࡹࠣࡉ࡙ࡧࡧࠡࡨࡲࡶࠥࡶࡥࡳࡥࡼࠦὖ"))
    except Exception as e:
      self.logger.error(bstack11l11l1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡧࡶࡦࠢࡷ࡬ࡪࠦࡥࡵࡣࡪ࠰ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣὗ").format(e))
  def bstack1lllll1llll1_opy_(self, bstack1111111l111_opy_):
    try:
      bstack11111111l1l_opy_ = self.bstack1lllll1l1l11_opy_(bstack1111111l111_opy_)
      if os.path.exists(bstack11111111l1l_opy_):
        with open(bstack11111111l1l_opy_, bstack11l11l1_opy_ (u"ࠤࡵࠦ὘")) as f:
          bstack1llllllll1ll_opy_ = f.read().strip()
          return bstack1llllllll1ll_opy_ if bstack1llllllll1ll_opy_ else None
    except Exception as e:
      self.logger.error(bstack11l11l1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡰࡴࡧࡤࡪࡰࡪࠤࡊ࡚ࡡࡨ࠮ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨὙ").format(e))
  def bstack11111111lll_opy_(self, bstack1111111l111_opy_, bstack11111111l11_opy_):
    bstack1111111ll1l_opy_ = self.bstack1lllll1llll1_opy_(bstack1111111l111_opy_)
    if bstack1111111ll1l_opy_:
      try:
        bstack1llllll1ll11_opy_ = self.bstack111111111ll_opy_(bstack1111111ll1l_opy_, bstack11111111l11_opy_)
        if not bstack1llllll1ll11_opy_:
          self.logger.debug(bstack11l11l1_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣ࡭ࡸࠦࡵࡱࠢࡷࡳࠥࡪࡡࡵࡧࠣࠬࡊ࡚ࡡࡨࠢࡸࡲࡨ࡮ࡡ࡯ࡩࡨࡨ࠮ࠨ὚"))
          return True
        self.logger.debug(bstack11l11l1_opy_ (u"ࠧࡔࡥࡸࠢࡓࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡤࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡺࡶࡤࡢࡶࡨࠦὛ"))
        return False
      except Exception as e:
        self.logger.warn(bstack11l11l1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡦ࡬ࡪࡩ࡫ࠡࡨࡲࡶࠥࡨࡩ࡯ࡣࡵࡽࠥࡻࡰࡥࡣࡷࡩࡸ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡥࡹ࡫ࡶࡸ࡮ࡴࡧࠡࡤ࡬ࡲࡦࡸࡹ࠻ࠢࡾࢁࠧ὜").format(e))
    return False
  def bstack111111111ll_opy_(self, bstack1111111ll1l_opy_, bstack11111111l11_opy_):
    try:
      headers = {
        bstack11l11l1_opy_ (u"ࠢࡊࡨ࠰ࡒࡴࡴࡥ࠮ࡏࡤࡸࡨ࡮ࠢὝ"): bstack1111111ll1l_opy_
      }
      response = bstack1ll1l1l11l_opy_(bstack11l11l1_opy_ (u"ࠨࡉࡈࡘࠬ὞"), bstack11111111l11_opy_, {}, {bstack11l11l1_opy_ (u"ࠤ࡫ࡩࡦࡪࡥࡳࡵࠥὟ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack11l11l1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡦ࡬ࡪࡩ࡫ࡪࡰࡪࠤ࡫ࡵࡲࠡࡒࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡶࡲࡧࡥࡹ࡫ࡳ࠻ࠢࡾࢁࠧὠ").format(e))
  @measure(event_name=EVENTS.bstack11l1l11l11l_opy_, stage=STAGE.bstack1ll1lllll_opy_)
  def bstack1lllllll1l11_opy_(self, bstack11111111l11_opy_, bstack1llllll11l11_opy_):
    try:
      bstack1lllll1l111l_opy_ = self.bstack11111111ll1_opy_()
      bstack1lllll1l11ll_opy_ = os.path.join(bstack1lllll1l111l_opy_, bstack11l11l1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻ࠱ࡾ࡮ࡶࠧὡ"))
      bstack1lllll1lll11_opy_ = os.path.join(bstack1lllll1l111l_opy_, bstack1llllll11l11_opy_)
      if self.bstack11111111lll_opy_(bstack1lllll1l111l_opy_, bstack11111111l11_opy_): # if bstack1lllll1ll111_opy_, bstack1llll1ll1ll_opy_ bstack1llllllll1ll_opy_ is bstack1lllll1l1l1l_opy_ to bstack111l1111lll_opy_ version available (response 304)
        if os.path.exists(bstack1lllll1lll11_opy_):
          self.logger.info(bstack11l11l1_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡻࡾ࠮ࠣࡷࡰ࡯ࡰࡱ࡫ࡱ࡫ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠢὢ").format(bstack1lllll1lll11_opy_))
          return bstack1lllll1lll11_opy_
        if os.path.exists(bstack1lllll1l11ll_opy_):
          self.logger.info(bstack11l11l1_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࢀࡩࡱࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࢀࢃࠬࠡࡷࡱࡾ࡮ࡶࡰࡪࡰࡪࠦὣ").format(bstack1lllll1l11ll_opy_))
          return self.bstack1llllll11111_opy_(bstack1lllll1l11ll_opy_, bstack1llllll11l11_opy_)
      self.logger.info(bstack11l11l1_opy_ (u"ࠢࡅࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫ࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤ࡫ࡸ࡯࡮ࠢࡾࢁࠧὤ").format(bstack11111111l11_opy_))
      response = bstack1ll1l1l11l_opy_(bstack11l11l1_opy_ (u"ࠨࡉࡈࡘࠬὥ"), bstack11111111l11_opy_, {}, {})
      if response.status_code == 200:
        bstack1llllllllll1_opy_ = response.headers.get(bstack11l11l1_opy_ (u"ࠤࡈࡘࡦ࡭ࠢὦ"), bstack11l11l1_opy_ (u"ࠥࠦὧ"))
        if bstack1llllllllll1_opy_:
          self.bstack1llllll1lll1_opy_(bstack1lllll1l111l_opy_, bstack1llllllllll1_opy_)
        with open(bstack1lllll1l11ll_opy_, bstack11l11l1_opy_ (u"ࠫࡼࡨࠧὨ")) as file:
          file.write(response.content)
        self.logger.info(bstack11l11l1_opy_ (u"ࠧࡊ࡯ࡸࡰ࡯ࡳࡦࡪࡥࡥࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡣࡱࡨࠥࡹࡡࡷࡧࡧࠤࡦࡺࠠࡼࡿࠥὩ").format(bstack1lllll1l11ll_opy_))
        return self.bstack1llllll11111_opy_(bstack1lllll1l11ll_opy_, bstack1llllll11l11_opy_)
      else:
        raise(bstack11l11l1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠤࡹ࡮ࡥࠡࡨ࡬ࡰࡪ࠴ࠠࡔࡶࡤࡸࡺࡹࠠࡤࡱࡧࡩ࠿ࠦࡻࡾࠤὪ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack11l11l1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼ࠾ࠥࢁࡽࠣὫ").format(e))
  def bstack1lllllllll1l_opy_(self, bstack11111111l11_opy_, bstack1llllll11l11_opy_):
    try:
      retry = 2
      bstack1lllll1lll11_opy_ = None
      bstack1lllllllll11_opy_ = False
      while retry > 0:
        bstack1lllll1lll11_opy_ = self.bstack1lllllll1l11_opy_(bstack11111111l11_opy_, bstack1llllll11l11_opy_)
        bstack1lllllllll11_opy_ = self.bstack1lllll1l1111_opy_(bstack11111111l11_opy_, bstack1llllll11l11_opy_, bstack1lllll1lll11_opy_)
        if bstack1lllllllll11_opy_:
          break
        retry -= 1
      return bstack1lllll1lll11_opy_, bstack1lllllllll11_opy_
    except Exception as e:
      self.logger.error(bstack11l11l1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡬࡫ࡴࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡱࡣࡷ࡬ࠧὬ").format(e))
    return bstack1lllll1lll11_opy_, False
  def bstack1lllll1l1111_opy_(self, bstack11111111l11_opy_, bstack1llllll11l11_opy_, bstack1lllll1lll11_opy_, bstack1lllll1ll1l1_opy_ = 0):
    if bstack1lllll1ll1l1_opy_ > 1:
      return False
    if bstack1lllll1lll11_opy_ == None or os.path.exists(bstack1lllll1lll11_opy_) == False:
      self.logger.warn(bstack11l11l1_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡲࡤࡸ࡭ࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥ࠮ࠣࡶࡪࡺࡲࡺ࡫ࡱ࡫ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠢὭ"))
      return False
    bstack1lllll1l1ll1_opy_ = bstack11l11l1_opy_ (u"ࡵࠦࡣ࠴ࠪࡁࡲࡨࡶࡨࡿ࠯ࡤ࡮࡬ࠤࡡࡪࠫ࡝࠰࡟ࡨ࠰ࡢ࠮࡝ࡦ࠮ࠦὮ")
    command = bstack11l11l1_opy_ (u"ࠫࢀࢃࠠ࠮࠯ࡹࡩࡷࡹࡩࡰࡰࠪὯ").format(bstack1lllll1lll11_opy_)
    bstack1lllll1l11l1_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1lllll1l1ll1_opy_, bstack1lllll1l11l1_opy_) != None:
      return True
    else:
      self.logger.error(bstack11l11l1_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥࡩࡨࡦࡥ࡮ࠤ࡫ࡧࡩ࡭ࡧࡧࠦὰ"))
      return False
  def bstack1llllll11111_opy_(self, bstack1lllll1l11ll_opy_, bstack1llllll11l11_opy_):
    try:
      working_dir = os.path.dirname(bstack1lllll1l11ll_opy_)
      shutil.unpack_archive(bstack1lllll1l11ll_opy_, working_dir)
      bstack1lllll1lll11_opy_ = os.path.join(working_dir, bstack1llllll11l11_opy_)
      os.chmod(bstack1lllll1lll11_opy_, 0o755)
      return bstack1lllll1lll11_opy_
    except Exception as e:
      self.logger.error(bstack11l11l1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡸࡲࡿ࡯ࡰࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠢά"))
  def bstack1111111111l_opy_(self):
    try:
      bstack1111111ll11_opy_ = self.config.get(bstack11l11l1_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ὲ"))
      bstack1111111111l_opy_ = bstack1111111ll11_opy_ or (bstack1111111ll11_opy_ is None and self.bstack11llll11ll_opy_)
      if not bstack1111111111l_opy_ or self.config.get(bstack11l11l1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫέ"), None) not in bstack11l1l1l1111_opy_:
        return False
      self.bstack1ll111111l_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack11l11l1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡦࡸࠥࡶࡥࡳࡥࡼ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦὴ").format(e))
  def bstack1llllll1l1l1_opy_(self):
    try:
      bstack1llllll1l1l1_opy_ = self.percy_capture_mode
      return bstack1llllll1l1l1_opy_
    except Exception as e:
      self.logger.error(bstack11l11l1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡦࡶࡨࡧࡹࠦࡰࡦࡴࡦࡽࠥࡩࡡࡱࡶࡸࡶࡪࠦ࡭ࡰࡦࡨ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦή").format(e))
  def init(self, bstack11llll11ll_opy_, config, logger):
    self.bstack11llll11ll_opy_ = bstack11llll11ll_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1111111111l_opy_():
      return
    self.bstack11111111111_opy_ = config.get(bstack11l11l1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡒࡴࡹ࡯࡯࡯ࡵࠪὶ"), {})
    self.percy_capture_mode = config.get(bstack11l11l1_opy_ (u"ࠬࡶࡥࡳࡥࡼࡇࡦࡶࡴࡶࡴࡨࡑࡴࡪࡥࠨί"))
    try:
      bstack11111111l11_opy_, bstack1llllll11l11_opy_ = self.bstack1lllll1l1lll_opy_()
      self.bstack111l1llll11_opy_ = bstack1llllll11l11_opy_
      bstack1lllll1lll11_opy_, bstack1lllllllll11_opy_ = self.bstack1lllllllll1l_opy_(bstack11111111l11_opy_, bstack1llllll11l11_opy_)
      if bstack1lllllllll11_opy_:
        self.binary_path = bstack1lllll1lll11_opy_
        thread = Thread(target=self.bstack1lllllll1l1l_opy_)
        thread.start()
      else:
        self.bstack1llllll1llll_opy_ = True
        self.logger.error(bstack11l11l1_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡱࡧࡵࡧࡾࠦࡰࡢࡶ࡫ࠤ࡫ࡵࡵ࡯ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡕ࡫ࡲࡤࡻࠥὸ").format(bstack1lllll1lll11_opy_))
    except Exception as e:
      self.logger.error(bstack11l11l1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣό").format(e))
  def bstack111111111l1_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack11l11l1_opy_ (u"ࠨ࡮ࡲ࡫ࠬὺ"), bstack11l11l1_opy_ (u"ࠩࡳࡩࡷࡩࡹ࠯࡮ࡲ࡫ࠬύ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack11l11l1_opy_ (u"ࠥࡔࡺࡹࡨࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡰࡴ࡭ࡳࠡࡣࡷࠤࢀࢃࠢὼ").format(logfile))
      self.bstack1111111l1ll_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack11l11l1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡧࡷࠤࡵ࡫ࡲࡤࡻࠣࡰࡴ࡭ࠠࡱࡣࡷ࡬࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧώ").format(e))
  @measure(event_name=EVENTS.bstack11l11ll1111_opy_, stage=STAGE.bstack1ll1lllll_opy_)
  def bstack1lllllll1l1l_opy_(self):
    bstack1111111l11l_opy_ = self.bstack1llllllll1l1_opy_()
    if bstack1111111l11l_opy_ == None:
      self.bstack1llllll1llll_opy_ = True
      self.logger.error(bstack11l11l1_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡹࡵ࡫ࡦࡰࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩ࠲ࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹࠣ὾"))
      return False
    bstack1111111lll1_opy_ = [bstack11l11l1_opy_ (u"ࠨࡡࡱࡲ࠽ࡩࡽ࡫ࡣ࠻ࡵࡷࡥࡷࡺࠢ὿") if self.bstack11llll11ll_opy_ else bstack11l11l1_opy_ (u"ࠧࡦࡺࡨࡧ࠿ࡹࡴࡢࡴࡷࠫᾀ")]
    bstack11111l1l1ll_opy_ = self.bstack1111111llll_opy_()
    if bstack11111l1l1ll_opy_ != None:
      bstack1111111lll1_opy_.append(bstack11l11l1_opy_ (u"ࠣ࠯ࡦࠤࢀࢃࠢᾁ").format(bstack11111l1l1ll_opy_))
    env = os.environ.copy()
    env[bstack11l11l1_opy_ (u"ࠤࡓࡉࡗࡉ࡙ࡠࡖࡒࡏࡊࡔࠢᾂ")] = bstack1111111l11l_opy_
    env[bstack11l11l1_opy_ (u"ࠥࡘࡍࡥࡂࡖࡋࡏࡈࡤ࡛ࡕࡊࡆࠥᾃ")] = os.environ.get(bstack11l11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᾄ"), bstack11l11l1_opy_ (u"ࠬ࠭ᾅ"))
    bstack1lllll1ll11l_opy_ = [self.binary_path]
    self.bstack111111111l1_opy_()
    self.bstack1lllll1lllll_opy_ = self.bstack1lllllll1ll1_opy_(bstack1lllll1ll11l_opy_ + bstack1111111lll1_opy_, env)
    self.logger.debug(bstack11l11l1_opy_ (u"ࠨࡓࡵࡣࡵࡸ࡮ࡴࡧࠡࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠢᾆ"))
    bstack1lllll1ll1l1_opy_ = 0
    while self.bstack1lllll1lllll_opy_.poll() == None:
      bstack1lllllll11l1_opy_ = self.bstack111111l1111_opy_()
      if bstack1lllllll11l1_opy_:
        self.logger.debug(bstack11l11l1_opy_ (u"ࠢࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠦࡳࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠥᾇ"))
        self.bstack1llllll1111l_opy_ = True
        return True
      bstack1lllll1ll1l1_opy_ += 1
      self.logger.debug(bstack11l11l1_opy_ (u"ࠣࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠠࡓࡧࡷࡶࡾࠦ࠭ࠡࡽࢀࠦᾈ").format(bstack1lllll1ll1l1_opy_))
      time.sleep(2)
    self.logger.error(bstack11l11l1_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡍ࡫ࡡ࡭ࡶ࡫ࠤࡈ࡮ࡥࡤ࡭ࠣࡊࡦ࡯࡬ࡦࡦࠣࡥ࡫ࡺࡥࡳࠢࡾࢁࠥࡧࡴࡵࡧࡰࡴࡹࡹࠢᾉ").format(bstack1lllll1ll1l1_opy_))
    self.bstack1llllll1llll_opy_ = True
    return False
  def bstack111111l1111_opy_(self, bstack1lllll1ll1l1_opy_ = 0):
    if bstack1lllll1ll1l1_opy_ > 10:
      return False
    try:
      bstack1llllll111l1_opy_ = os.environ.get(bstack11l11l1_opy_ (u"ࠪࡔࡊࡘࡃ࡚ࡡࡖࡉࡗ࡜ࡅࡓࡡࡄࡈࡉࡘࡅࡔࡕࠪᾊ"), bstack11l11l1_opy_ (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳ࡱࡵࡣࡢ࡮࡫ࡳࡸࡺ࠺࠶࠵࠶࠼ࠬᾋ"))
      bstack1lllll1lll1l_opy_ = bstack1llllll111l1_opy_ + bstack11l1l11l111_opy_
      response = requests.get(bstack1lllll1lll1l_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack11l11l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࠫᾌ"), {}).get(bstack11l11l1_opy_ (u"࠭ࡩࡥࠩᾍ"), None)
      return True
    except:
      self.logger.debug(bstack11l11l1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦ࡯ࡤࡥࡸࡶࡷ࡫ࡤࠡࡹ࡫࡭ࡱ࡫ࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤ࡭࡫ࡡ࡭ࡶ࡫ࠤࡨ࡮ࡥࡤ࡭ࠣࡶࡪࡹࡰࡰࡰࡶࡩࠧᾎ"))
      return False
  def bstack1llllllll1l1_opy_(self):
    bstack1111111l1l1_opy_ = bstack11l11l1_opy_ (u"ࠨࡣࡳࡴࠬᾏ") if self.bstack11llll11ll_opy_ else bstack11l11l1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫᾐ")
    bstack1lllllll111l_opy_ = bstack11l11l1_opy_ (u"ࠥࡹࡳࡪࡥࡧ࡫ࡱࡩࡩࠨᾑ") if self.config.get(bstack11l11l1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪᾒ")) is None else True
    bstack11ll11l1l11_opy_ = bstack11l11l1_opy_ (u"ࠧࡧࡰࡪ࠱ࡤࡴࡵࡥࡰࡦࡴࡦࡽ࠴࡭ࡥࡵࡡࡳࡶࡴࡰࡥࡤࡶࡢࡸࡴࡱࡥ࡯ࡁࡱࡥࡲ࡫࠽ࡼࡿࠩࡸࡾࡶࡥ࠾ࡽࢀࠪࡵ࡫ࡲࡤࡻࡀࡿࢂࠨᾓ").format(self.config[bstack11l11l1_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᾔ")], bstack1111111l1l1_opy_, bstack1lllllll111l_opy_)
    if self.percy_capture_mode:
      bstack11ll11l1l11_opy_ += bstack11l11l1_opy_ (u"ࠢࠧࡲࡨࡶࡨࡿ࡟ࡤࡣࡳࡸࡺࡸࡥࡠ࡯ࡲࡨࡪࡃࡻࡾࠤᾕ").format(self.percy_capture_mode)
    uri = bstack1l111111l1_opy_(bstack11ll11l1l11_opy_)
    try:
      response = bstack1ll1l1l11l_opy_(bstack11l11l1_opy_ (u"ࠨࡉࡈࡘࠬᾖ"), uri, {}, {bstack11l11l1_opy_ (u"ࠩࡤࡹࡹ࡮ࠧᾗ"): (self.config[bstack11l11l1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬᾘ")], self.config[bstack11l11l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧᾙ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack1ll111111l_opy_ = data.get(bstack11l11l1_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭ᾚ"))
        self.percy_capture_mode = data.get(bstack11l11l1_opy_ (u"࠭ࡰࡦࡴࡦࡽࡤࡩࡡࡱࡶࡸࡶࡪࡥ࡭ࡰࡦࡨࠫᾛ"))
        os.environ[bstack11l11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࠬᾜ")] = str(self.bstack1ll111111l_opy_)
        os.environ[bstack11l11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞ࡥࡃࡂࡒࡗ࡙ࡗࡋ࡟ࡎࡑࡇࡉࠬᾝ")] = str(self.percy_capture_mode)
        if bstack1lllllll111l_opy_ == bstack11l11l1_opy_ (u"ࠤࡸࡲࡩ࡫ࡦࡪࡰࡨࡨࠧᾞ") and str(self.bstack1ll111111l_opy_).lower() == bstack11l11l1_opy_ (u"ࠥࡸࡷࡻࡥࠣᾟ"):
          self.bstack11llllll1l_opy_ = True
        if bstack11l11l1_opy_ (u"ࠦࡹࡵ࡫ࡦࡰࠥᾠ") in data:
          return data[bstack11l11l1_opy_ (u"ࠧࡺ࡯࡬ࡧࡱࠦᾡ")]
        else:
          raise bstack11l11l1_opy_ (u"࠭ࡔࡰ࡭ࡨࡲࠥࡔ࡯ࡵࠢࡉࡳࡺࡴࡤࠡ࠯ࠣࡿࢂ࠭ᾢ").format(data)
      else:
        raise bstack11l11l1_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡪࡪࡺࡣࡩࠢࡳࡩࡷࡩࡹࠡࡶࡲ࡯ࡪࡴࠬࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡷࡹࡧࡴࡶࡵࠣ࠱ࠥࢁࡽ࠭ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨࠤࡇࡵࡤࡺࠢ࠰ࠤࢀࢃࠢᾣ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack11l11l1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡࡲࡵࡳ࡯࡫ࡣࡵࠤᾤ").format(e))
  def bstack1111111llll_opy_(self):
    bstack1llllllll11l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11l1_opy_ (u"ࠤࡳࡩࡷࡩࡹࡄࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠧᾥ"))
    try:
      if bstack11l11l1_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫᾦ") not in self.bstack11111111111_opy_:
        self.bstack11111111111_opy_[bstack11l11l1_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬᾧ")] = 2
      with open(bstack1llllllll11l_opy_, bstack11l11l1_opy_ (u"ࠬࡽࠧᾨ")) as fp:
        json.dump(self.bstack11111111111_opy_, fp)
      return bstack1llllllll11l_opy_
    except Exception as e:
      self.logger.error(bstack11l11l1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡦࡶࡪࡧࡴࡦࠢࡳࡩࡷࡩࡹࠡࡥࡲࡲ࡫࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᾩ").format(e))
  def bstack1lllllll1ll1_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1llllll11lll_opy_ == bstack11l11l1_opy_ (u"ࠧࡸ࡫ࡱࠫᾪ"):
        bstack1lllllllllll_opy_ = [bstack11l11l1_opy_ (u"ࠨࡥࡰࡨ࠳࡫ࡸࡦࠩᾫ"), bstack11l11l1_opy_ (u"ࠩ࠲ࡧࠬᾬ")]
        cmd = bstack1lllllllllll_opy_ + cmd
      cmd = bstack11l11l1_opy_ (u"ࠪࠤࠬᾭ").join(cmd)
      self.logger.debug(bstack11l11l1_opy_ (u"ࠦࡗࡻ࡮࡯࡫ࡱ࡫ࠥࢁࡽࠣᾮ").format(cmd))
      with open(self.bstack1111111l1ll_opy_, bstack11l11l1_opy_ (u"ࠧࡧࠢᾯ")) as bstack1lllllll1111_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1lllllll1111_opy_, text=True, stderr=bstack1lllllll1111_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1llllll1llll_opy_ = True
      self.logger.error(bstack11l11l1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠠࡸ࡫ࡷ࡬ࠥࡩ࡭ࡥࠢ࠰ࠤࢀࢃࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࢁࡽࠣᾰ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1llllll1111l_opy_:
        self.logger.info(bstack11l11l1_opy_ (u"ࠢࡔࡶࡲࡴࡵ࡯࡮ࡨࠢࡓࡩࡷࡩࡹࠣᾱ"))
        cmd = [self.binary_path, bstack11l11l1_opy_ (u"ࠣࡧࡻࡩࡨࡀࡳࡵࡱࡳࠦᾲ")]
        self.bstack1lllllll1ll1_opy_(cmd)
        self.bstack1llllll1111l_opy_ = False
    except Exception as e:
      self.logger.error(bstack11l11l1_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡰࡲࠣࡷࡪࡹࡳࡪࡱࡱࠤࡼ࡯ࡴࡩࠢࡦࡳࡲࡳࡡ࡯ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤᾳ").format(cmd, e))
  def bstack111ll111l_opy_(self):
    if not self.bstack1ll111111l_opy_:
      return
    try:
      bstack1llllllll111_opy_ = 0
      while not self.bstack1llllll1111l_opy_ and bstack1llllllll111_opy_ < self.bstack1lllllll11ll_opy_:
        if self.bstack1llllll1llll_opy_:
          self.logger.info(bstack11l11l1_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡶࡩࡹࡻࡰࠡࡨࡤ࡭ࡱ࡫ࡤࠣᾴ"))
          return
        time.sleep(1)
        bstack1llllllll111_opy_ += 1
      os.environ[bstack11l11l1_opy_ (u"ࠫࡕࡋࡒࡄ࡛ࡢࡆࡊ࡙ࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࠪ᾵")] = str(self.bstack1llllll1l11l_opy_())
      self.logger.info(bstack11l11l1_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡸ࡫ࡴࡶࡲࠣࡧࡴࡳࡰ࡭ࡧࡷࡩࡩࠨᾶ"))
    except Exception as e:
      self.logger.error(bstack11l11l1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡩࡹࡻࡰࠡࡲࡨࡶࡨࡿࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᾷ").format(e))
  def bstack1llllll1l11l_opy_(self):
    if self.bstack11llll11ll_opy_:
      return
    try:
      bstack1llllll1l111_opy_ = [platform[bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬᾸ")].lower() for platform in self.config.get(bstack11l11l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫᾹ"), [])]
      bstack1llllll11l1l_opy_ = sys.maxsize
      bstack111111l111l_opy_ = bstack11l11l1_opy_ (u"ࠩࠪᾺ")
      for browser in bstack1llllll1l111_opy_:
        if browser in self.bstack1llllll111ll_opy_:
          bstack1llllll1l1ll_opy_ = self.bstack1llllll111ll_opy_[browser]
        if bstack1llllll1l1ll_opy_ < bstack1llllll11l1l_opy_:
          bstack1llllll11l1l_opy_ = bstack1llllll1l1ll_opy_
          bstack111111l111l_opy_ = browser
      return bstack111111l111l_opy_
    except Exception as e:
      self.logger.error(bstack11l11l1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡪࡰࡧࠤࡧ࡫ࡳࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦΆ").format(e))
  @classmethod
  def bstack1l11ll1111_opy_(self):
    return os.getenv(bstack11l11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࠩᾼ"), bstack11l11l1_opy_ (u"ࠬࡌࡡ࡭ࡵࡨࠫ᾽")).lower()
  @classmethod
  def bstack1l1ll11111_opy_(self):
    return os.getenv(bstack11l11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࡣࡈࡇࡐࡕࡗࡕࡉࡤࡓࡏࡅࡇࠪι"), bstack11l11l1_opy_ (u"ࠧࠨ᾿"))
  @classmethod
  def bstack11lllll1l1l_opy_(cls, value):
    cls.bstack11llllll1l_opy_ = value
  @classmethod
  def bstack1lllll1ll1ll_opy_(cls):
    return cls.bstack11llllll1l_opy_
  @classmethod
  def bstack11lllll11l1_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack1lllllll1lll_opy_(cls):
    return cls.percy_build_id