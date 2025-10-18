# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
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
from bstack_utils.helper import bstack1ll1l1lll_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11llll1l11_opy_ import bstack1lll11l111_opy_
class bstack111l1l1ll1_opy_:
  working_dir = os.getcwd()
  bstack11ll11l11_opy_ = False
  config = {}
  bstack111l111llll_opy_ = bstack11ll_opy_ (u"ࠪࠫὋ")
  binary_path = bstack11ll_opy_ (u"ࠫࠬὌ")
  bstack1lllll1ll111_opy_ = bstack11ll_opy_ (u"ࠬ࠭Ὅ")
  bstack111l1ll11l_opy_ = False
  bstack1lllll1lll11_opy_ = None
  bstack1llllll11lll_opy_ = {}
  bstack1lllll1llll1_opy_ = 300
  bstack1lllll1l1lll_opy_ = False
  logger = None
  bstack1111111ll11_opy_ = False
  bstack11l1lll11_opy_ = False
  percy_build_id = None
  bstack1lllll1lll1l_opy_ = bstack11ll_opy_ (u"࠭ࠧ὎")
  bstack1lllll1ll1l1_opy_ = {
    bstack11ll_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ὏") : 1,
    bstack11ll_opy_ (u"ࠨࡨ࡬ࡶࡪ࡬࡯ࡹࠩὐ") : 2,
    bstack11ll_opy_ (u"ࠩࡨࡨ࡬࡫ࠧὑ") : 3,
    bstack11ll_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪὒ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1111111l1l1_opy_(self):
    bstack11111111lll_opy_ = bstack11ll_opy_ (u"ࠫࠬὓ")
    bstack1lllll1l1l1l_opy_ = sys.platform
    bstack1lllllllllll_opy_ = bstack11ll_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫὔ")
    if re.match(bstack11ll_opy_ (u"ࠨࡤࡢࡴࡺ࡭ࡳࢂ࡭ࡢࡥࠣࡳࡸࠨὕ"), bstack1lllll1l1l1l_opy_) != None:
      bstack11111111lll_opy_ = bstack11l1l11l1ll_opy_ + bstack11ll_opy_ (u"ࠢ࠰ࡲࡨࡶࡨࡿ࠭ࡰࡵࡻ࠲ࡿ࡯ࡰࠣὖ")
      self.bstack1lllll1lll1l_opy_ = bstack11ll_opy_ (u"ࠨ࡯ࡤࡧࠬὗ")
    elif re.match(bstack11ll_opy_ (u"ࠤࡰࡷࡼ࡯࡮ࡽ࡯ࡶࡽࡸࢂ࡭ࡪࡰࡪࡻࢁࡩࡹࡨࡹ࡬ࡲࢁࡨࡣࡤࡹ࡬ࡲࢁࡽࡩ࡯ࡥࡨࢀࡪࡳࡣࡽࡹ࡬ࡲ࠸࠸ࠢ὘"), bstack1lllll1l1l1l_opy_) != None:
      bstack11111111lll_opy_ = bstack11l1l11l1ll_opy_ + bstack11ll_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠰ࡻ࡮ࡴ࠮ࡻ࡫ࡳࠦὙ")
      bstack1lllllllllll_opy_ = bstack11ll_opy_ (u"ࠦࡵ࡫ࡲࡤࡻ࠱ࡩࡽ࡫ࠢ὚")
      self.bstack1lllll1lll1l_opy_ = bstack11ll_opy_ (u"ࠬࡽࡩ࡯ࠩὛ")
    else:
      bstack11111111lll_opy_ = bstack11l1l11l1ll_opy_ + bstack11ll_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠳࡬ࡪࡰࡸࡼ࠳ࢀࡩࡱࠤ὜")
      self.bstack1lllll1lll1l_opy_ = bstack11ll_opy_ (u"ࠧ࡭࡫ࡱࡹࡽ࠭Ὕ")
    return bstack11111111lll_opy_, bstack1lllllllllll_opy_
  def bstack11111111l1l_opy_(self):
    try:
      bstack1111111lll1_opy_ = [os.path.join(expanduser(bstack11ll_opy_ (u"ࠣࢀࠥ὞")), bstack11ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩὟ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1111111lll1_opy_:
        if(self.bstack1lllllll11l1_opy_(path)):
          return path
      raise bstack11ll_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠢὠ")
    except Exception as e:
      self.logger.error(bstack11ll_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥࠡࡲࡤࡸ࡭ࠦࡦࡰࡴࠣࡴࡪࡸࡣࡺࠢࡧࡳࡼࡴ࡬ࡰࡣࡧ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࠯ࠣࡿࢂࠨὡ").format(e))
  def bstack1lllllll11l1_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1llllllll1ll_opy_(self, bstack111111111ll_opy_):
    return os.path.join(bstack111111111ll_opy_, self.bstack111l111llll_opy_ + bstack11ll_opy_ (u"ࠧ࠴ࡥࡵࡣࡪࠦὢ"))
  def bstack1lllllll1ll1_opy_(self, bstack111111111ll_opy_, bstack1lllll1l1ll1_opy_):
    if not bstack1lllll1l1ll1_opy_: return
    try:
      bstack1llllll1l111_opy_ = self.bstack1llllllll1ll_opy_(bstack111111111ll_opy_)
      with open(bstack1llllll1l111_opy_, bstack11ll_opy_ (u"ࠨࡷࠣὣ")) as f:
        f.write(bstack1lllll1l1ll1_opy_)
        self.logger.debug(bstack11ll_opy_ (u"ࠢࡔࡣࡹࡩࡩࠦ࡮ࡦࡹࠣࡉ࡙ࡧࡧࠡࡨࡲࡶࠥࡶࡥࡳࡥࡼࠦὤ"))
    except Exception as e:
      self.logger.error(bstack11ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡧࡶࡦࠢࡷ࡬ࡪࠦࡥࡵࡣࡪ࠰ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣὥ").format(e))
  def bstack1llllll1ll11_opy_(self, bstack111111111ll_opy_):
    try:
      bstack1llllll1l111_opy_ = self.bstack1llllllll1ll_opy_(bstack111111111ll_opy_)
      if os.path.exists(bstack1llllll1l111_opy_):
        with open(bstack1llllll1l111_opy_, bstack11ll_opy_ (u"ࠤࡵࠦὦ")) as f:
          bstack1lllll1l1ll1_opy_ = f.read().strip()
          return bstack1lllll1l1ll1_opy_ if bstack1lllll1l1ll1_opy_ else None
    except Exception as e:
      self.logger.error(bstack11ll_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡰࡴࡧࡤࡪࡰࡪࠤࡊ࡚ࡡࡨ࠮ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨὧ").format(e))
  def bstack1llllll1l1ll_opy_(self, bstack111111111ll_opy_, bstack11111111lll_opy_):
    bstack11111111ll1_opy_ = self.bstack1llllll1ll11_opy_(bstack111111111ll_opy_)
    if bstack11111111ll1_opy_:
      try:
        bstack11111111l11_opy_ = self.bstack1lllll11llll_opy_(bstack11111111ll1_opy_, bstack11111111lll_opy_)
        if not bstack11111111l11_opy_:
          self.logger.debug(bstack11ll_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣ࡭ࡸࠦࡵࡱࠢࡷࡳࠥࡪࡡࡵࡧࠣࠬࡊ࡚ࡡࡨࠢࡸࡲࡨ࡮ࡡ࡯ࡩࡨࡨ࠮ࠨὨ"))
          return True
        self.logger.debug(bstack11ll_opy_ (u"ࠧࡔࡥࡸࠢࡓࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡤࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡺࡶࡤࡢࡶࡨࠦὩ"))
        return False
      except Exception as e:
        self.logger.warn(bstack11ll_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡦ࡬ࡪࡩ࡫ࠡࡨࡲࡶࠥࡨࡩ࡯ࡣࡵࡽࠥࡻࡰࡥࡣࡷࡩࡸ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡥࡹ࡫ࡶࡸ࡮ࡴࡧࠡࡤ࡬ࡲࡦࡸࡹ࠻ࠢࡾࢁࠧὪ").format(e))
    return False
  def bstack1lllll11llll_opy_(self, bstack11111111ll1_opy_, bstack11111111lll_opy_):
    try:
      headers = {
        bstack11ll_opy_ (u"ࠢࡊࡨ࠰ࡒࡴࡴࡥ࠮ࡏࡤࡸࡨ࡮ࠢὫ"): bstack11111111ll1_opy_
      }
      response = bstack1ll1l1lll_opy_(bstack11ll_opy_ (u"ࠨࡉࡈࡘࠬὬ"), bstack11111111lll_opy_, {}, {bstack11ll_opy_ (u"ࠤ࡫ࡩࡦࡪࡥࡳࡵࠥὭ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack11ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡦ࡬ࡪࡩ࡫ࡪࡰࡪࠤ࡫ࡵࡲࠡࡒࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡶࡲࡧࡥࡹ࡫ࡳ࠻ࠢࡾࢁࠧὮ").format(e))
  @measure(event_name=EVENTS.bstack11l1l11ll1l_opy_, stage=STAGE.bstack1ll1111l1_opy_)
  def bstack1llllll1llll_opy_(self, bstack11111111lll_opy_, bstack1lllllllllll_opy_):
    try:
      bstack1lllll1l11l1_opy_ = self.bstack11111111l1l_opy_()
      bstack1llllll1l11l_opy_ = os.path.join(bstack1lllll1l11l1_opy_, bstack11ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻ࠱ࡾ࡮ࡶࠧὯ"))
      bstack1llllll1lll1_opy_ = os.path.join(bstack1lllll1l11l1_opy_, bstack1lllllllllll_opy_)
      if self.bstack1llllll1l1ll_opy_(bstack1lllll1l11l1_opy_, bstack11111111lll_opy_): # if bstack1111111l1ll_opy_, bstack1llllllll11_opy_ bstack1lllll1l1ll1_opy_ is bstack1lllll1ll1ll_opy_ to bstack1111llll1l1_opy_ version available (response 304)
        if os.path.exists(bstack1llllll1lll1_opy_):
          self.logger.info(bstack11ll_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡻࡾ࠮ࠣࡷࡰ࡯ࡰࡱ࡫ࡱ࡫ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠢὰ").format(bstack1llllll1lll1_opy_))
          return bstack1llllll1lll1_opy_
        if os.path.exists(bstack1llllll1l11l_opy_):
          self.logger.info(bstack11ll_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࢀࡩࡱࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࢀࢃࠬࠡࡷࡱࡾ࡮ࡶࡰࡪࡰࡪࠦά").format(bstack1llllll1l11l_opy_))
          return self.bstack1lllll1ll11l_opy_(bstack1llllll1l11l_opy_, bstack1lllllllllll_opy_)
      self.logger.info(bstack11ll_opy_ (u"ࠢࡅࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫ࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤ࡫ࡸ࡯࡮ࠢࡾࢁࠧὲ").format(bstack11111111lll_opy_))
      response = bstack1ll1l1lll_opy_(bstack11ll_opy_ (u"ࠨࡉࡈࡘࠬέ"), bstack11111111lll_opy_, {}, {})
      if response.status_code == 200:
        bstack1lllll1lllll_opy_ = response.headers.get(bstack11ll_opy_ (u"ࠤࡈࡘࡦ࡭ࠢὴ"), bstack11ll_opy_ (u"ࠥࠦή"))
        if bstack1lllll1lllll_opy_:
          self.bstack1lllllll1ll1_opy_(bstack1lllll1l11l1_opy_, bstack1lllll1lllll_opy_)
        with open(bstack1llllll1l11l_opy_, bstack11ll_opy_ (u"ࠫࡼࡨࠧὶ")) as file:
          file.write(response.content)
        self.logger.info(bstack11ll_opy_ (u"ࠧࡊ࡯ࡸࡰ࡯ࡳࡦࡪࡥࡥࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡣࡱࡨࠥࡹࡡࡷࡧࡧࠤࡦࡺࠠࡼࡿࠥί").format(bstack1llllll1l11l_opy_))
        return self.bstack1lllll1ll11l_opy_(bstack1llllll1l11l_opy_, bstack1lllllllllll_opy_)
      else:
        raise(bstack11ll_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠤࡹ࡮ࡥࠡࡨ࡬ࡰࡪ࠴ࠠࡔࡶࡤࡸࡺࡹࠠࡤࡱࡧࡩ࠿ࠦࡻࡾࠤὸ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack11ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼ࠾ࠥࢁࡽࠣό").format(e))
  def bstack1llllll1ll1l_opy_(self, bstack11111111lll_opy_, bstack1lllllllllll_opy_):
    try:
      retry = 2
      bstack1llllll1lll1_opy_ = None
      bstack1llllllll11l_opy_ = False
      while retry > 0:
        bstack1llllll1lll1_opy_ = self.bstack1llllll1llll_opy_(bstack11111111lll_opy_, bstack1lllllllllll_opy_)
        bstack1llllllll11l_opy_ = self.bstack1lllllll1l1l_opy_(bstack11111111lll_opy_, bstack1lllllllllll_opy_, bstack1llllll1lll1_opy_)
        if bstack1llllllll11l_opy_:
          break
        retry -= 1
      return bstack1llllll1lll1_opy_, bstack1llllllll11l_opy_
    except Exception as e:
      self.logger.error(bstack11ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡬࡫ࡴࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡱࡣࡷ࡬ࠧὺ").format(e))
    return bstack1llllll1lll1_opy_, False
  def bstack1lllllll1l1l_opy_(self, bstack11111111lll_opy_, bstack1lllllllllll_opy_, bstack1llllll1lll1_opy_, bstack1llllll111l1_opy_ = 0):
    if bstack1llllll111l1_opy_ > 1:
      return False
    if bstack1llllll1lll1_opy_ == None or os.path.exists(bstack1llllll1lll1_opy_) == False:
      self.logger.warn(bstack11ll_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡲࡤࡸ࡭ࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥ࠮ࠣࡶࡪࡺࡲࡺ࡫ࡱ࡫ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠢύ"))
      return False
    bstack111111111l1_opy_ = bstack11ll_opy_ (u"ࡵࠦࡣ࠴ࠪࡁࡲࡨࡶࡨࡿ࠯ࡤ࡮࡬ࠤࡡࡪࠫ࡝࠰࡟ࡨ࠰ࡢ࠮࡝ࡦ࠮ࠦὼ")
    command = bstack11ll_opy_ (u"ࠫࢀࢃࠠ࠮࠯ࡹࡩࡷࡹࡩࡰࡰࠪώ").format(bstack1llllll1lll1_opy_)
    bstack1111111ll1l_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack111111111l1_opy_, bstack1111111ll1l_opy_) != None:
      return True
    else:
      self.logger.error(bstack11ll_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥࡩࡨࡦࡥ࡮ࠤ࡫ࡧࡩ࡭ࡧࡧࠦ὾"))
      return False
  def bstack1lllll1ll11l_opy_(self, bstack1llllll1l11l_opy_, bstack1lllllllllll_opy_):
    try:
      working_dir = os.path.dirname(bstack1llllll1l11l_opy_)
      shutil.unpack_archive(bstack1llllll1l11l_opy_, working_dir)
      bstack1llllll1lll1_opy_ = os.path.join(working_dir, bstack1lllllllllll_opy_)
      os.chmod(bstack1llllll1lll1_opy_, 0o755)
      return bstack1llllll1lll1_opy_
    except Exception as e:
      self.logger.error(bstack11ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡸࡲࡿ࡯ࡰࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠢ὿"))
  def bstack1lllllll1lll_opy_(self):
    try:
      bstack1lllllllll1l_opy_ = self.config.get(bstack11ll_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ᾀ"))
      bstack1lllllll1lll_opy_ = bstack1lllllllll1l_opy_ or (bstack1lllllllll1l_opy_ is None and self.bstack11ll11l11_opy_)
      if not bstack1lllllll1lll_opy_ or self.config.get(bstack11ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫᾁ"), None) not in bstack11l11lll11l_opy_:
        return False
      self.bstack111l1ll11l_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack11ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡦࡸࠥࡶࡥࡳࡥࡼ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᾂ").format(e))
  def bstack1llllll111ll_opy_(self):
    try:
      bstack1llllll111ll_opy_ = self.percy_capture_mode
      return bstack1llllll111ll_opy_
    except Exception as e:
      self.logger.error(bstack11ll_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡦࡶࡨࡧࡹࠦࡰࡦࡴࡦࡽࠥࡩࡡࡱࡶࡸࡶࡪࠦ࡭ࡰࡦࡨ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᾃ").format(e))
  def init(self, bstack11ll11l11_opy_, config, logger):
    self.bstack11ll11l11_opy_ = bstack11ll11l11_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1lllllll1lll_opy_():
      return
    self.bstack1llllll11lll_opy_ = config.get(bstack11ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᾄ"), {})
    self.percy_capture_mode = config.get(bstack11ll_opy_ (u"ࠬࡶࡥࡳࡥࡼࡇࡦࡶࡴࡶࡴࡨࡑࡴࡪࡥࠨᾅ"))
    try:
      bstack11111111lll_opy_, bstack1lllllllllll_opy_ = self.bstack1111111l1l1_opy_()
      self.bstack111l111llll_opy_ = bstack1lllllllllll_opy_
      bstack1llllll1lll1_opy_, bstack1llllllll11l_opy_ = self.bstack1llllll1ll1l_opy_(bstack11111111lll_opy_, bstack1lllllllllll_opy_)
      if bstack1llllllll11l_opy_:
        self.binary_path = bstack1llllll1lll1_opy_
        thread = Thread(target=self.bstack1llllllllll1_opy_)
        thread.start()
      else:
        self.bstack1111111ll11_opy_ = True
        self.logger.error(bstack11ll_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡱࡧࡵࡧࡾࠦࡰࡢࡶ࡫ࠤ࡫ࡵࡵ࡯ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡕ࡫ࡲࡤࡻࠥᾆ").format(bstack1llllll1lll1_opy_))
    except Exception as e:
      self.logger.error(bstack11ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᾇ").format(e))
  def bstack1llllllll1l1_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack11ll_opy_ (u"ࠨ࡮ࡲ࡫ࠬᾈ"), bstack11ll_opy_ (u"ࠩࡳࡩࡷࡩࡹ࠯࡮ࡲ࡫ࠬᾉ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack11ll_opy_ (u"ࠥࡔࡺࡹࡨࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡰࡴ࡭ࡳࠡࡣࡷࠤࢀࢃࠢᾊ").format(logfile))
      self.bstack1lllll1ll111_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack11ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡧࡷࠤࡵ࡫ࡲࡤࡻࠣࡰࡴ࡭ࠠࡱࡣࡷ࡬࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᾋ").format(e))
  @measure(event_name=EVENTS.bstack11l11l1l1ll_opy_, stage=STAGE.bstack1ll1111l1_opy_)
  def bstack1llllllllll1_opy_(self):
    bstack1lllll11ll11_opy_ = self.bstack1lllll1l1l11_opy_()
    if bstack1lllll11ll11_opy_ == None:
      self.bstack1111111ll11_opy_ = True
      self.logger.error(bstack11ll_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡹࡵ࡫ࡦࡰࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩ࠲ࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹࠣᾌ"))
      return False
    bstack1llllllll111_opy_ = [bstack11ll_opy_ (u"ࠨࡡࡱࡲ࠽ࡩࡽ࡫ࡣ࠻ࡵࡷࡥࡷࡺࠢᾍ") if self.bstack11ll11l11_opy_ else bstack11ll_opy_ (u"ࠧࡦࡺࡨࡧ࠿ࡹࡴࡢࡴࡷࠫᾎ")]
    bstack11111l1llll_opy_ = self.bstack1lllll1l1111_opy_()
    if bstack11111l1llll_opy_ != None:
      bstack1llllllll111_opy_.append(bstack11ll_opy_ (u"ࠣ࠯ࡦࠤࢀࢃࠢᾏ").format(bstack11111l1llll_opy_))
    env = os.environ.copy()
    env[bstack11ll_opy_ (u"ࠤࡓࡉࡗࡉ࡙ࡠࡖࡒࡏࡊࡔࠢᾐ")] = bstack1lllll11ll11_opy_
    env[bstack11ll_opy_ (u"ࠥࡘࡍࡥࡂࡖࡋࡏࡈࡤ࡛ࡕࡊࡆࠥᾑ")] = os.environ.get(bstack11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᾒ"), bstack11ll_opy_ (u"ࠬ࠭ᾓ"))
    bstack1lllllll111l_opy_ = [self.binary_path]
    self.bstack1llllllll1l1_opy_()
    self.bstack1lllll1lll11_opy_ = self.bstack1llllll11ll1_opy_(bstack1lllllll111l_opy_ + bstack1llllllll111_opy_, env)
    self.logger.debug(bstack11ll_opy_ (u"ࠨࡓࡵࡣࡵࡸ࡮ࡴࡧࠡࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠢᾔ"))
    bstack1llllll111l1_opy_ = 0
    while self.bstack1lllll1lll11_opy_.poll() == None:
      bstack1lllll1l111l_opy_ = self.bstack1111111111l_opy_()
      if bstack1lllll1l111l_opy_:
        self.logger.debug(bstack11ll_opy_ (u"ࠢࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠦࡳࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠥᾕ"))
        self.bstack1lllll1l1lll_opy_ = True
        return True
      bstack1llllll111l1_opy_ += 1
      self.logger.debug(bstack11ll_opy_ (u"ࠣࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠠࡓࡧࡷࡶࡾࠦ࠭ࠡࡽࢀࠦᾖ").format(bstack1llllll111l1_opy_))
      time.sleep(2)
    self.logger.error(bstack11ll_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡍ࡫ࡡ࡭ࡶ࡫ࠤࡈ࡮ࡥࡤ࡭ࠣࡊࡦ࡯࡬ࡦࡦࠣࡥ࡫ࡺࡥࡳࠢࡾࢁࠥࡧࡴࡵࡧࡰࡴࡹࡹࠢᾗ").format(bstack1llllll111l1_opy_))
    self.bstack1111111ll11_opy_ = True
    return False
  def bstack1111111111l_opy_(self, bstack1llllll111l1_opy_ = 0):
    if bstack1llllll111l1_opy_ > 10:
      return False
    try:
      bstack1llllll1111l_opy_ = os.environ.get(bstack11ll_opy_ (u"ࠪࡔࡊࡘࡃ࡚ࡡࡖࡉࡗ࡜ࡅࡓࡡࡄࡈࡉࡘࡅࡔࡕࠪᾘ"), bstack11ll_opy_ (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳ࡱࡵࡣࡢ࡮࡫ࡳࡸࡺ࠺࠶࠵࠶࠼ࠬᾙ"))
      bstack1111111l111_opy_ = bstack1llllll1111l_opy_ + bstack11l1l11111l_opy_
      response = requests.get(bstack1111111l111_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࠫᾚ"), {}).get(bstack11ll_opy_ (u"࠭ࡩࡥࠩᾛ"), None)
      return True
    except:
      self.logger.debug(bstack11ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦ࡯ࡤࡥࡸࡶࡷ࡫ࡤࠡࡹ࡫࡭ࡱ࡫ࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤ࡭࡫ࡡ࡭ࡶ࡫ࠤࡨ࡮ࡥࡤ࡭ࠣࡶࡪࡹࡰࡰࡰࡶࡩࠧᾜ"))
      return False
  def bstack1lllll1l1l11_opy_(self):
    bstack1llllll11111_opy_ = bstack11ll_opy_ (u"ࠨࡣࡳࡴࠬᾝ") if self.bstack11ll11l11_opy_ else bstack11ll_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫᾞ")
    bstack1llllll11l11_opy_ = bstack11ll_opy_ (u"ࠥࡹࡳࡪࡥࡧ࡫ࡱࡩࡩࠨᾟ") if self.config.get(bstack11ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪᾠ")) is None else True
    bstack11ll111l11l_opy_ = bstack11ll_opy_ (u"ࠧࡧࡰࡪ࠱ࡤࡴࡵࡥࡰࡦࡴࡦࡽ࠴࡭ࡥࡵࡡࡳࡶࡴࡰࡥࡤࡶࡢࡸࡴࡱࡥ࡯ࡁࡱࡥࡲ࡫࠽ࡼࡿࠩࡸࡾࡶࡥ࠾ࡽࢀࠪࡵ࡫ࡲࡤࡻࡀࡿࢂࠨᾡ").format(self.config[bstack11ll_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᾢ")], bstack1llllll11111_opy_, bstack1llllll11l11_opy_)
    if self.percy_capture_mode:
      bstack11ll111l11l_opy_ += bstack11ll_opy_ (u"ࠢࠧࡲࡨࡶࡨࡿ࡟ࡤࡣࡳࡸࡺࡸࡥࡠ࡯ࡲࡨࡪࡃࡻࡾࠤᾣ").format(self.percy_capture_mode)
    uri = bstack1lll11l111_opy_(bstack11ll111l11l_opy_)
    try:
      response = bstack1ll1l1lll_opy_(bstack11ll_opy_ (u"ࠨࡉࡈࡘࠬᾤ"), uri, {}, {bstack11ll_opy_ (u"ࠩࡤࡹࡹ࡮ࠧᾥ"): (self.config[bstack11ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬᾦ")], self.config[bstack11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧᾧ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack111l1ll11l_opy_ = data.get(bstack11ll_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭ᾨ"))
        self.percy_capture_mode = data.get(bstack11ll_opy_ (u"࠭ࡰࡦࡴࡦࡽࡤࡩࡡࡱࡶࡸࡶࡪࡥ࡭ࡰࡦࡨࠫᾩ"))
        os.environ[bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࠬᾪ")] = str(self.bstack111l1ll11l_opy_)
        os.environ[bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞ࡥࡃࡂࡒࡗ࡙ࡗࡋ࡟ࡎࡑࡇࡉࠬᾫ")] = str(self.percy_capture_mode)
        if bstack1llllll11l11_opy_ == bstack11ll_opy_ (u"ࠤࡸࡲࡩ࡫ࡦࡪࡰࡨࡨࠧᾬ") and str(self.bstack111l1ll11l_opy_).lower() == bstack11ll_opy_ (u"ࠥࡸࡷࡻࡥࠣᾭ"):
          self.bstack11l1lll11_opy_ = True
        if bstack11ll_opy_ (u"ࠦࡹࡵ࡫ࡦࡰࠥᾮ") in data:
          return data[bstack11ll_opy_ (u"ࠧࡺ࡯࡬ࡧࡱࠦᾯ")]
        else:
          raise bstack11ll_opy_ (u"࠭ࡔࡰ࡭ࡨࡲࠥࡔ࡯ࡵࠢࡉࡳࡺࡴࡤࠡ࠯ࠣࡿࢂ࠭ᾰ").format(data)
      else:
        raise bstack11ll_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡪࡪࡺࡣࡩࠢࡳࡩࡷࡩࡹࠡࡶࡲ࡯ࡪࡴࠬࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡷࡹࡧࡴࡶࡵࠣ࠱ࠥࢁࡽ࠭ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨࠤࡇࡵࡤࡺࠢ࠰ࠤࢀࢃࠢᾱ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack11ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡࡲࡵࡳ࡯࡫ࡣࡵࠤᾲ").format(e))
  def bstack1lllll1l1111_opy_(self):
    bstack1lllll11ll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll_opy_ (u"ࠤࡳࡩࡷࡩࡹࡄࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠧᾳ"))
    try:
      if bstack11ll_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫᾴ") not in self.bstack1llllll11lll_opy_:
        self.bstack1llllll11lll_opy_[bstack11ll_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬ᾵")] = 2
      with open(bstack1lllll11ll1l_opy_, bstack11ll_opy_ (u"ࠬࡽࠧᾶ")) as fp:
        json.dump(self.bstack1llllll11lll_opy_, fp)
      return bstack1lllll11ll1l_opy_
    except Exception as e:
      self.logger.error(bstack11ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡦࡶࡪࡧࡴࡦࠢࡳࡩࡷࡩࡹࠡࡥࡲࡲ࡫࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᾷ").format(e))
  def bstack1llllll11ll1_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1lllll1lll1l_opy_ == bstack11ll_opy_ (u"ࠧࡸ࡫ࡱࠫᾸ"):
        bstack1llllll11l1l_opy_ = [bstack11ll_opy_ (u"ࠨࡥࡰࡨ࠳࡫ࡸࡦࠩᾹ"), bstack11ll_opy_ (u"ࠩ࠲ࡧࠬᾺ")]
        cmd = bstack1llllll11l1l_opy_ + cmd
      cmd = bstack11ll_opy_ (u"ࠪࠤࠬΆ").join(cmd)
      self.logger.debug(bstack11ll_opy_ (u"ࠦࡗࡻ࡮࡯࡫ࡱ࡫ࠥࢁࡽࠣᾼ").format(cmd))
      with open(self.bstack1lllll1ll111_opy_, bstack11ll_opy_ (u"ࠧࡧࠢ᾽")) as bstack11111111111_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack11111111111_opy_, text=True, stderr=bstack11111111111_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1111111ll11_opy_ = True
      self.logger.error(bstack11ll_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠠࡸ࡫ࡷ࡬ࠥࡩ࡭ࡥࠢ࠰ࠤࢀࢃࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࢁࡽࠣι").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1lllll1l1lll_opy_:
        self.logger.info(bstack11ll_opy_ (u"ࠢࡔࡶࡲࡴࡵ࡯࡮ࡨࠢࡓࡩࡷࡩࡹࠣ᾿"))
        cmd = [self.binary_path, bstack11ll_opy_ (u"ࠣࡧࡻࡩࡨࡀࡳࡵࡱࡳࠦ῀")]
        self.bstack1llllll11ll1_opy_(cmd)
        self.bstack1lllll1l1lll_opy_ = False
    except Exception as e:
      self.logger.error(bstack11ll_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡰࡲࠣࡷࡪࡹࡳࡪࡱࡱࠤࡼ࡯ࡴࡩࠢࡦࡳࡲࡳࡡ࡯ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤ῁").format(cmd, e))
  def bstack111l11lll_opy_(self):
    if not self.bstack111l1ll11l_opy_:
      return
    try:
      bstack1111111l11l_opy_ = 0
      while not self.bstack1lllll1l1lll_opy_ and bstack1111111l11l_opy_ < self.bstack1lllll1llll1_opy_:
        if self.bstack1111111ll11_opy_:
          self.logger.info(bstack11ll_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡶࡩࡹࡻࡰࠡࡨࡤ࡭ࡱ࡫ࡤࠣῂ"))
          return
        time.sleep(1)
        bstack1111111l11l_opy_ += 1
      os.environ[bstack11ll_opy_ (u"ࠫࡕࡋࡒࡄ࡛ࡢࡆࡊ࡙ࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࠪῃ")] = str(self.bstack1lllllllll11_opy_())
      self.logger.info(bstack11ll_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡸ࡫ࡴࡶࡲࠣࡧࡴࡳࡰ࡭ࡧࡷࡩࡩࠨῄ"))
    except Exception as e:
      self.logger.error(bstack11ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡩࡹࡻࡰࠡࡲࡨࡶࡨࡿࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢ῅").format(e))
  def bstack1lllllllll11_opy_(self):
    if self.bstack11ll11l11_opy_:
      return
    try:
      bstack1lllll1l11ll_opy_ = [platform[bstack11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬῆ")].lower() for platform in self.config.get(bstack11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫῇ"), [])]
      bstack1llllll1l1l1_opy_ = sys.maxsize
      bstack1lllllll1111_opy_ = bstack11ll_opy_ (u"ࠩࠪῈ")
      for browser in bstack1lllll1l11ll_opy_:
        if browser in self.bstack1lllll1ll1l1_opy_:
          bstack1lllllll1l11_opy_ = self.bstack1lllll1ll1l1_opy_[browser]
        if bstack1lllllll1l11_opy_ < bstack1llllll1l1l1_opy_:
          bstack1llllll1l1l1_opy_ = bstack1lllllll1l11_opy_
          bstack1lllllll1111_opy_ = browser
      return bstack1lllllll1111_opy_
    except Exception as e:
      self.logger.error(bstack11ll_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡪࡰࡧࠤࡧ࡫ࡳࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦΈ").format(e))
  @classmethod
  def bstack1l1llll1l1_opy_(self):
    return os.getenv(bstack11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࠩῊ"), bstack11ll_opy_ (u"ࠬࡌࡡ࡭ࡵࡨࠫΉ")).lower()
  @classmethod
  def bstack11111lllll_opy_(self):
    return os.getenv(bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࡣࡈࡇࡐࡕࡗࡕࡉࡤࡓࡏࡅࡇࠪῌ"), bstack11ll_opy_ (u"ࠧࠨ῍"))
  @classmethod
  def bstack11lllll1l11_opy_(cls, value):
    cls.bstack11l1lll11_opy_ = value
  @classmethod
  def bstack1lllllll11ll_opy_(cls):
    return cls.bstack11l1lll11_opy_
  @classmethod
  def bstack11lllll1l1l_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack1lllll11lll1_opy_(cls):
    return cls.percy_build_id