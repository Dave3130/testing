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
from bstack_utils.helper import bstack1l11l1111_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l11ll111_opy_ import bstack11111lll11_opy_
class bstack11l11lll11_opy_:
  working_dir = os.getcwd()
  bstack1l1ll1lll_opy_ = False
  config = {}
  bstack111l11lllll_opy_ = bstack1lll11l_opy_ (u"ࠪࠫὠ")
  binary_path = bstack1lll11l_opy_ (u"ࠫࠬὡ")
  bstack1llllll1l1ll_opy_ = bstack1lll11l_opy_ (u"ࠬ࠭ὢ")
  bstack1ll11lll1l_opy_ = False
  bstack1llllll1l111_opy_ = None
  bstack1lllllll1l1l_opy_ = {}
  bstack11111111ll1_opy_ = 300
  bstack1llllll1111l_opy_ = False
  logger = None
  bstack1llllllll1l1_opy_ = False
  bstack11l1111l1l_opy_ = False
  percy_build_id = None
  bstack1llllll1l11l_opy_ = bstack1lll11l_opy_ (u"࠭ࠧὣ")
  bstack1llllll1llll_opy_ = {
    bstack1lll11l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧὤ") : 1,
    bstack1lll11l_opy_ (u"ࠨࡨ࡬ࡶࡪ࡬࡯ࡹࠩὥ") : 2,
    bstack1lll11l_opy_ (u"ࠩࡨࡨ࡬࡫ࠧὦ") : 3,
    bstack1lll11l_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪὧ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1lllllll1l11_opy_(self):
    bstack1lllll11llll_opy_ = bstack1lll11l_opy_ (u"ࠫࠬὨ")
    bstack11111111lll_opy_ = sys.platform
    bstack1llllllll1ll_opy_ = bstack1lll11l_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫὩ")
    if re.match(bstack1lll11l_opy_ (u"ࠨࡤࡢࡴࡺ࡭ࡳࢂ࡭ࡢࡥࠣࡳࡸࠨὪ"), bstack11111111lll_opy_) != None:
      bstack1lllll11llll_opy_ = bstack11l1l11l1l1_opy_ + bstack1lll11l_opy_ (u"ࠢ࠰ࡲࡨࡶࡨࡿ࠭ࡰࡵࡻ࠲ࡿ࡯ࡰࠣὫ")
      self.bstack1llllll1l11l_opy_ = bstack1lll11l_opy_ (u"ࠨ࡯ࡤࡧࠬὬ")
    elif re.match(bstack1lll11l_opy_ (u"ࠤࡰࡷࡼ࡯࡮ࡽ࡯ࡶࡽࡸࢂ࡭ࡪࡰࡪࡻࢁࡩࡹࡨࡹ࡬ࡲࢁࡨࡣࡤࡹ࡬ࡲࢁࡽࡩ࡯ࡥࡨࢀࡪࡳࡣࡽࡹ࡬ࡲ࠸࠸ࠢὭ"), bstack11111111lll_opy_) != None:
      bstack1lllll11llll_opy_ = bstack11l1l11l1l1_opy_ + bstack1lll11l_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠰ࡻ࡮ࡴ࠮ࡻ࡫ࡳࠦὮ")
      bstack1llllllll1ll_opy_ = bstack1lll11l_opy_ (u"ࠦࡵ࡫ࡲࡤࡻ࠱ࡩࡽ࡫ࠢὯ")
      self.bstack1llllll1l11l_opy_ = bstack1lll11l_opy_ (u"ࠬࡽࡩ࡯ࠩὰ")
    else:
      bstack1lllll11llll_opy_ = bstack11l1l11l1l1_opy_ + bstack1lll11l_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠳࡬ࡪࡰࡸࡼ࠳ࢀࡩࡱࠤά")
      self.bstack1llllll1l11l_opy_ = bstack1lll11l_opy_ (u"ࠧ࡭࡫ࡱࡹࡽ࠭ὲ")
    return bstack1lllll11llll_opy_, bstack1llllllll1ll_opy_
  def bstack1lllll11ll11_opy_(self):
    try:
      bstack1llllll111ll_opy_ = [os.path.join(expanduser(bstack1lll11l_opy_ (u"ࠣࢀࠥέ")), bstack1lll11l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩὴ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1llllll111ll_opy_:
        if(self.bstack1lllll1ll111_opy_(path)):
          return path
      raise bstack1lll11l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠢή")
    except Exception as e:
      self.logger.error(bstack1lll11l_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥࠡࡲࡤࡸ࡭ࠦࡦࡰࡴࠣࡴࡪࡸࡣࡺࠢࡧࡳࡼࡴ࡬ࡰࡣࡧ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࠯ࠣࡿࢂࠨὶ").format(e))
  def bstack1lllll1ll111_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1llllllll111_opy_(self, bstack1lllll1ll11l_opy_):
    return os.path.join(bstack1lllll1ll11l_opy_, self.bstack111l11lllll_opy_ + bstack1lll11l_opy_ (u"ࠧ࠴ࡥࡵࡣࡪࠦί"))
  def bstack1llllll11l1l_opy_(self, bstack1lllll1ll11l_opy_, bstack1lllll1l1l1l_opy_):
    if not bstack1lllll1l1l1l_opy_: return
    try:
      bstack1lllllll11l1_opy_ = self.bstack1llllllll111_opy_(bstack1lllll1ll11l_opy_)
      with open(bstack1lllllll11l1_opy_, bstack1lll11l_opy_ (u"ࠨࡷࠣὸ")) as f:
        f.write(bstack1lllll1l1l1l_opy_)
        self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡔࡣࡹࡩࡩࠦ࡮ࡦࡹࠣࡉ࡙ࡧࡧࠡࡨࡲࡶࠥࡶࡥࡳࡥࡼࠦό"))
    except Exception as e:
      self.logger.error(bstack1lll11l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡧࡶࡦࠢࡷ࡬ࡪࠦࡥࡵࡣࡪ࠰ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣὺ").format(e))
  def bstack1lllllllll11_opy_(self, bstack1lllll1ll11l_opy_):
    try:
      bstack1lllllll11l1_opy_ = self.bstack1llllllll111_opy_(bstack1lllll1ll11l_opy_)
      if os.path.exists(bstack1lllllll11l1_opy_):
        with open(bstack1lllllll11l1_opy_, bstack1lll11l_opy_ (u"ࠤࡵࠦύ")) as f:
          bstack1lllll1l1l1l_opy_ = f.read().strip()
          return bstack1lllll1l1l1l_opy_ if bstack1lllll1l1l1l_opy_ else None
    except Exception as e:
      self.logger.error(bstack1lll11l_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡰࡴࡧࡤࡪࡰࡪࠤࡊ࡚ࡡࡨ࠮ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨὼ").format(e))
  def bstack1lllll1ll1l1_opy_(self, bstack1lllll1ll11l_opy_, bstack1lllll11llll_opy_):
    bstack1lllllllllll_opy_ = self.bstack1lllllllll11_opy_(bstack1lllll1ll11l_opy_)
    if bstack1lllllllllll_opy_:
      try:
        bstack11111111111_opy_ = self.bstack1lllll1lll11_opy_(bstack1lllllllllll_opy_, bstack1lllll11llll_opy_)
        if not bstack11111111111_opy_:
          self.logger.debug(bstack1lll11l_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣ࡭ࡸࠦࡵࡱࠢࡷࡳࠥࡪࡡࡵࡧࠣࠬࡊ࡚ࡡࡨࠢࡸࡲࡨ࡮ࡡ࡯ࡩࡨࡨ࠮ࠨώ"))
          return True
        self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡔࡥࡸࠢࡓࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡤࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡺࡶࡤࡢࡶࡨࠦ὾"))
        return False
      except Exception as e:
        self.logger.warn(bstack1lll11l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡦ࡬ࡪࡩ࡫ࠡࡨࡲࡶࠥࡨࡩ࡯ࡣࡵࡽࠥࡻࡰࡥࡣࡷࡩࡸ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡥࡹ࡫ࡶࡸ࡮ࡴࡧࠡࡤ࡬ࡲࡦࡸࡹ࠻ࠢࡾࢁࠧ὿").format(e))
    return False
  def bstack1lllll1lll11_opy_(self, bstack1lllllllllll_opy_, bstack1lllll11llll_opy_):
    try:
      headers = {
        bstack1lll11l_opy_ (u"ࠢࡊࡨ࠰ࡒࡴࡴࡥ࠮ࡏࡤࡸࡨ࡮ࠢᾀ"): bstack1lllllllllll_opy_
      }
      response = bstack1l11l1111_opy_(bstack1lll11l_opy_ (u"ࠨࡉࡈࡘࠬᾁ"), bstack1lllll11llll_opy_, {}, {bstack1lll11l_opy_ (u"ࠤ࡫ࡩࡦࡪࡥࡳࡵࠥᾂ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack1lll11l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡦ࡬ࡪࡩ࡫ࡪࡰࡪࠤ࡫ࡵࡲࠡࡒࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡶࡲࡧࡥࡹ࡫ࡳ࠻ࠢࡾࢁࠧᾃ").format(e))
  @measure(event_name=EVENTS.bstack11l1l11llll_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
  def bstack1lllll1l1111_opy_(self, bstack1lllll11llll_opy_, bstack1llllllll1ll_opy_):
    try:
      bstack1llllll1ll1l_opy_ = self.bstack1lllll11ll11_opy_()
      bstack111111111l1_opy_ = os.path.join(bstack1llllll1ll1l_opy_, bstack1lll11l_opy_ (u"ࠫࡵ࡫ࡲࡤࡻ࠱ࡾ࡮ࡶࠧᾄ"))
      bstack1llllll11l11_opy_ = os.path.join(bstack1llllll1ll1l_opy_, bstack1llllllll1ll_opy_)
      if self.bstack1lllll1ll1l1_opy_(bstack1llllll1ll1l_opy_, bstack1lllll11llll_opy_): # if bstack11111111l11_opy_, bstack111111111l_opy_ bstack1lllll1l1l1l_opy_ is bstack1lllll11lll1_opy_ to bstack1111ll1111l_opy_ version available (response 304)
        if os.path.exists(bstack1llllll11l11_opy_):
          self.logger.info(bstack1lll11l_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡻࡾ࠮ࠣࡷࡰ࡯ࡰࡱ࡫ࡱ࡫ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠢᾅ").format(bstack1llllll11l11_opy_))
          return bstack1llllll11l11_opy_
        if os.path.exists(bstack111111111l1_opy_):
          self.logger.info(bstack1lll11l_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࢀࡩࡱࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࢀࢃࠬࠡࡷࡱࡾ࡮ࡶࡰࡪࡰࡪࠦᾆ").format(bstack111111111l1_opy_))
          return self.bstack1lllll1lll1l_opy_(bstack111111111l1_opy_, bstack1llllllll1ll_opy_)
      self.logger.info(bstack1lll11l_opy_ (u"ࠢࡅࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫ࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤ࡫ࡸ࡯࡮ࠢࡾࢁࠧᾇ").format(bstack1lllll11llll_opy_))
      response = bstack1l11l1111_opy_(bstack1lll11l_opy_ (u"ࠨࡉࡈࡘࠬᾈ"), bstack1lllll11llll_opy_, {}, {})
      if response.status_code == 200:
        bstack1lllll11l1ll_opy_ = response.headers.get(bstack1lll11l_opy_ (u"ࠤࡈࡘࡦ࡭ࠢᾉ"), bstack1lll11l_opy_ (u"ࠥࠦᾊ"))
        if bstack1lllll11l1ll_opy_:
          self.bstack1llllll11l1l_opy_(bstack1llllll1ll1l_opy_, bstack1lllll11l1ll_opy_)
        with open(bstack111111111l1_opy_, bstack1lll11l_opy_ (u"ࠫࡼࡨࠧᾋ")) as file:
          file.write(response.content)
        self.logger.info(bstack1lll11l_opy_ (u"ࠧࡊ࡯ࡸࡰ࡯ࡳࡦࡪࡥࡥࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡣࡱࡨࠥࡹࡡࡷࡧࡧࠤࡦࡺࠠࡼࡿࠥᾌ").format(bstack111111111l1_opy_))
        return self.bstack1lllll1lll1l_opy_(bstack111111111l1_opy_, bstack1llllllll1ll_opy_)
      else:
        raise(bstack1lll11l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠤࡹ࡮ࡥࠡࡨ࡬ࡰࡪ࠴ࠠࡔࡶࡤࡸࡺࡹࠠࡤࡱࡧࡩ࠿ࠦࡻࡾࠤᾍ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack1lll11l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼ࠾ࠥࢁࡽࠣᾎ").format(e))
  def bstack1llllll1l1l1_opy_(self, bstack1lllll11llll_opy_, bstack1llllllll1ll_opy_):
    try:
      retry = 2
      bstack1llllll11l11_opy_ = None
      bstack1111111l1l1_opy_ = False
      while retry > 0:
        bstack1llllll11l11_opy_ = self.bstack1lllll1l1111_opy_(bstack1lllll11llll_opy_, bstack1llllllll1ll_opy_)
        bstack1111111l1l1_opy_ = self.bstack1lllll11l1l1_opy_(bstack1lllll11llll_opy_, bstack1llllllll1ll_opy_, bstack1llllll11l11_opy_)
        if bstack1111111l1l1_opy_:
          break
        retry -= 1
      return bstack1llllll11l11_opy_, bstack1111111l1l1_opy_
    except Exception as e:
      self.logger.error(bstack1lll11l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡬࡫ࡴࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡱࡣࡷ࡬ࠧᾏ").format(e))
    return bstack1llllll11l11_opy_, False
  def bstack1lllll11l1l1_opy_(self, bstack1lllll11llll_opy_, bstack1llllllll1ll_opy_, bstack1llllll11l11_opy_, bstack1lllll11ll1l_opy_ = 0):
    if bstack1lllll11ll1l_opy_ > 1:
      return False
    if bstack1llllll11l11_opy_ == None or os.path.exists(bstack1llllll11l11_opy_) == False:
      self.logger.warn(bstack1lll11l_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡲࡤࡸ࡭ࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥ࠮ࠣࡶࡪࡺࡲࡺ࡫ࡱ࡫ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠢᾐ"))
      return False
    bstack1lllll1ll1ll_opy_ = bstack1lll11l_opy_ (u"ࡵࠦࡣ࠴ࠪࡁࡲࡨࡶࡨࡿ࠯ࡤ࡮࡬ࠤࡡࡪࠫ࡝࠰࡟ࡨ࠰ࡢ࠮࡝ࡦ࠮ࠦᾑ")
    command = bstack1lll11l_opy_ (u"ࠫࢀࢃࠠ࠮࠯ࡹࡩࡷࡹࡩࡰࡰࠪᾒ").format(bstack1llllll11l11_opy_)
    bstack1lllll1lllll_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1lllll1ll1ll_opy_, bstack1lllll1lllll_opy_) != None:
      return True
    else:
      self.logger.error(bstack1lll11l_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥࡩࡨࡦࡥ࡮ࠤ࡫ࡧࡩ࡭ࡧࡧࠦᾓ"))
      return False
  def bstack1lllll1lll1l_opy_(self, bstack111111111l1_opy_, bstack1llllllll1ll_opy_):
    try:
      working_dir = os.path.dirname(bstack111111111l1_opy_)
      shutil.unpack_archive(bstack111111111l1_opy_, working_dir)
      bstack1llllll11l11_opy_ = os.path.join(working_dir, bstack1llllllll1ll_opy_)
      os.chmod(bstack1llllll11l11_opy_, 0o755)
      return bstack1llllll11l11_opy_
    except Exception as e:
      self.logger.error(bstack1lll11l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡸࡲࡿ࡯ࡰࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠢᾔ"))
  def bstack1lllllll11ll_opy_(self):
    try:
      bstack1llllll11ll1_opy_ = self.config.get(bstack1lll11l_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ᾕ"))
      bstack1lllllll11ll_opy_ = bstack1llllll11ll1_opy_ or (bstack1llllll11ll1_opy_ is None and self.bstack1l1ll1lll_opy_)
      if not bstack1lllllll11ll_opy_ or self.config.get(bstack1lll11l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫᾖ"), None) not in bstack11l11l1ll1l_opy_:
        return False
      self.bstack1ll11lll1l_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack1lll11l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡦࡸࠥࡶࡥࡳࡥࡼ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᾗ").format(e))
  def bstack1lllll11l11l_opy_(self):
    try:
      bstack1lllll11l11l_opy_ = self.percy_capture_mode
      return bstack1lllll11l11l_opy_
    except Exception as e:
      self.logger.error(bstack1lll11l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡦࡶࡨࡧࡹࠦࡰࡦࡴࡦࡽࠥࡩࡡࡱࡶࡸࡶࡪࠦ࡭ࡰࡦࡨ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᾘ").format(e))
  def init(self, bstack1l1ll1lll_opy_, config, logger):
    self.bstack1l1ll1lll_opy_ = bstack1l1ll1lll_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1lllllll11ll_opy_():
      return
    self.bstack1lllllll1l1l_opy_ = config.get(bstack1lll11l_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᾙ"), {})
    self.percy_capture_mode = config.get(bstack1lll11l_opy_ (u"ࠬࡶࡥࡳࡥࡼࡇࡦࡶࡴࡶࡴࡨࡑࡴࡪࡥࠨᾚ"))
    try:
      bstack1lllll11llll_opy_, bstack1llllllll1ll_opy_ = self.bstack1lllllll1l11_opy_()
      self.bstack111l11lllll_opy_ = bstack1llllllll1ll_opy_
      bstack1llllll11l11_opy_, bstack1111111l1l1_opy_ = self.bstack1llllll1l1l1_opy_(bstack1lllll11llll_opy_, bstack1llllllll1ll_opy_)
      if bstack1111111l1l1_opy_:
        self.binary_path = bstack1llllll11l11_opy_
        thread = Thread(target=self.bstack1lllll1l1ll1_opy_)
        thread.start()
      else:
        self.bstack1llllllll1l1_opy_ = True
        self.logger.error(bstack1lll11l_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡱࡧࡵࡧࡾࠦࡰࡢࡶ࡫ࠤ࡫ࡵࡵ࡯ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡕ࡫ࡲࡤࡻࠥᾛ").format(bstack1llllll11l11_opy_))
    except Exception as e:
      self.logger.error(bstack1lll11l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᾜ").format(e))
  def bstack1lllll1l1l11_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack1lll11l_opy_ (u"ࠨ࡮ࡲ࡫ࠬᾝ"), bstack1lll11l_opy_ (u"ࠩࡳࡩࡷࡩࡹ࠯࡮ࡲ࡫ࠬᾞ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack1lll11l_opy_ (u"ࠥࡔࡺࡹࡨࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡰࡴ࡭ࡳࠡࡣࡷࠤࢀࢃࠢᾟ").format(logfile))
      self.bstack1llllll1l1ll_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack1lll11l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡧࡷࠤࡵ࡫ࡲࡤࡻࠣࡰࡴ࡭ࠠࡱࡣࡷ࡬࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᾠ").format(e))
  @measure(event_name=EVENTS.bstack11l11ll1l1l_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
  def bstack1lllll1l1ll1_opy_(self):
    bstack1llllll1lll1_opy_ = self.bstack1llllll111l1_opy_()
    if bstack1llllll1lll1_opy_ == None:
      self.bstack1llllllll1l1_opy_ = True
      self.logger.error(bstack1lll11l_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡹࡵ࡫ࡦࡰࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩ࠲ࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹࠣᾡ"))
      return False
    bstack1111111111l_opy_ = [bstack1lll11l_opy_ (u"ࠨࡡࡱࡲ࠽ࡩࡽ࡫ࡣ࠻ࡵࡷࡥࡷࡺࠢᾢ") if self.bstack1l1ll1lll_opy_ else bstack1lll11l_opy_ (u"ࠧࡦࡺࡨࡧ࠿ࡹࡴࡢࡴࡷࠫᾣ")]
    bstack11111l1l111_opy_ = self.bstack11111111l1l_opy_()
    if bstack11111l1l111_opy_ != None:
      bstack1111111111l_opy_.append(bstack1lll11l_opy_ (u"ࠣ࠯ࡦࠤࢀࢃࠢᾤ").format(bstack11111l1l111_opy_))
    env = os.environ.copy()
    env[bstack1lll11l_opy_ (u"ࠤࡓࡉࡗࡉ࡙ࡠࡖࡒࡏࡊࡔࠢᾥ")] = bstack1llllll1lll1_opy_
    env[bstack1lll11l_opy_ (u"ࠥࡘࡍࡥࡂࡖࡋࡏࡈࡤ࡛ࡕࡊࡆࠥᾦ")] = os.environ.get(bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᾧ"), bstack1lll11l_opy_ (u"ࠬ࠭ᾨ"))
    bstack1lllllllll1l_opy_ = [self.binary_path]
    self.bstack1lllll1l1l11_opy_()
    self.bstack1llllll1l111_opy_ = self.bstack1llllll1ll11_opy_(bstack1lllllllll1l_opy_ + bstack1111111111l_opy_, env)
    self.logger.debug(bstack1lll11l_opy_ (u"ࠨࡓࡵࡣࡵࡸ࡮ࡴࡧࠡࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠢᾩ"))
    bstack1lllll11ll1l_opy_ = 0
    while self.bstack1llllll1l111_opy_.poll() == None:
      bstack1lllllll1lll_opy_ = self.bstack1lllll11l111_opy_()
      if bstack1lllllll1lll_opy_:
        self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠦࡳࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠥᾪ"))
        self.bstack1llllll1111l_opy_ = True
        return True
      bstack1lllll11ll1l_opy_ += 1
      self.logger.debug(bstack1lll11l_opy_ (u"ࠣࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠠࡓࡧࡷࡶࡾࠦ࠭ࠡࡽࢀࠦᾫ").format(bstack1lllll11ll1l_opy_))
      time.sleep(2)
    self.logger.error(bstack1lll11l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡍ࡫ࡡ࡭ࡶ࡫ࠤࡈ࡮ࡥࡤ࡭ࠣࡊࡦ࡯࡬ࡦࡦࠣࡥ࡫ࡺࡥࡳࠢࡾࢁࠥࡧࡴࡵࡧࡰࡴࡹࡹࠢᾬ").format(bstack1lllll11ll1l_opy_))
    self.bstack1llllllll1l1_opy_ = True
    return False
  def bstack1lllll11l111_opy_(self, bstack1lllll11ll1l_opy_ = 0):
    if bstack1lllll11ll1l_opy_ > 10:
      return False
    try:
      bstack1llllllllll1_opy_ = os.environ.get(bstack1lll11l_opy_ (u"ࠪࡔࡊࡘࡃ࡚ࡡࡖࡉࡗ࡜ࡅࡓࡡࡄࡈࡉࡘࡅࡔࡕࠪᾭ"), bstack1lll11l_opy_ (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳ࡱࡵࡣࡢ࡮࡫ࡳࡸࡺ࠺࠶࠵࠶࠼ࠬᾮ"))
      bstack1lllllll111l_opy_ = bstack1llllllllll1_opy_ + bstack11l11lll111_opy_
      response = requests.get(bstack1lllllll111l_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack1lll11l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࠫᾯ"), {}).get(bstack1lll11l_opy_ (u"࠭ࡩࡥࠩᾰ"), None)
      return True
    except:
      self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦ࡯ࡤࡥࡸࡶࡷ࡫ࡤࠡࡹ࡫࡭ࡱ࡫ࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤ࡭࡫ࡡ࡭ࡶ࡫ࠤࡨ࡮ࡥࡤ࡭ࠣࡶࡪࡹࡰࡰࡰࡶࡩࠧᾱ"))
      return False
  def bstack1llllll111l1_opy_(self):
    bstack1111111l11l_opy_ = bstack1lll11l_opy_ (u"ࠨࡣࡳࡴࠬᾲ") if self.bstack1l1ll1lll_opy_ else bstack1lll11l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫᾳ")
    bstack1lllll1l11ll_opy_ = bstack1lll11l_opy_ (u"ࠥࡹࡳࡪࡥࡧ࡫ࡱࡩࡩࠨᾴ") if self.config.get(bstack1lll11l_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪ᾵")) is None else True
    bstack11ll111l1ll_opy_ = bstack1lll11l_opy_ (u"ࠧࡧࡰࡪ࠱ࡤࡴࡵࡥࡰࡦࡴࡦࡽ࠴࡭ࡥࡵࡡࡳࡶࡴࡰࡥࡤࡶࡢࡸࡴࡱࡥ࡯ࡁࡱࡥࡲ࡫࠽ࡼࡿࠩࡸࡾࡶࡥ࠾ࡽࢀࠪࡵ࡫ࡲࡤࡻࡀࡿࢂࠨᾶ").format(self.config[bstack1lll11l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᾷ")], bstack1111111l11l_opy_, bstack1lllll1l11ll_opy_)
    if self.percy_capture_mode:
      bstack11ll111l1ll_opy_ += bstack1lll11l_opy_ (u"ࠢࠧࡲࡨࡶࡨࡿ࡟ࡤࡣࡳࡸࡺࡸࡥࡠ࡯ࡲࡨࡪࡃࡻࡾࠤᾸ").format(self.percy_capture_mode)
    uri = bstack11111lll11_opy_(bstack11ll111l1ll_opy_)
    try:
      response = bstack1l11l1111_opy_(bstack1lll11l_opy_ (u"ࠨࡉࡈࡘࠬᾹ"), uri, {}, {bstack1lll11l_opy_ (u"ࠩࡤࡹࡹ࡮ࠧᾺ"): (self.config[bstack1lll11l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬΆ")], self.config[bstack1lll11l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧᾼ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack1ll11lll1l_opy_ = data.get(bstack1lll11l_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭᾽"))
        self.percy_capture_mode = data.get(bstack1lll11l_opy_ (u"࠭ࡰࡦࡴࡦࡽࡤࡩࡡࡱࡶࡸࡶࡪࡥ࡭ࡰࡦࡨࠫι"))
        os.environ[bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࠬ᾿")] = str(self.bstack1ll11lll1l_opy_)
        os.environ[bstack1lll11l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞ࡥࡃࡂࡒࡗ࡙ࡗࡋ࡟ࡎࡑࡇࡉࠬ῀")] = str(self.percy_capture_mode)
        if bstack1lllll1l11ll_opy_ == bstack1lll11l_opy_ (u"ࠤࡸࡲࡩ࡫ࡦࡪࡰࡨࡨࠧ῁") and str(self.bstack1ll11lll1l_opy_).lower() == bstack1lll11l_opy_ (u"ࠥࡸࡷࡻࡥࠣῂ"):
          self.bstack11l1111l1l_opy_ = True
        if bstack1lll11l_opy_ (u"ࠦࡹࡵ࡫ࡦࡰࠥῃ") in data:
          return data[bstack1lll11l_opy_ (u"ࠧࡺ࡯࡬ࡧࡱࠦῄ")]
        else:
          raise bstack1lll11l_opy_ (u"࠭ࡔࡰ࡭ࡨࡲࠥࡔ࡯ࡵࠢࡉࡳࡺࡴࡤࠡ࠯ࠣࡿࢂ࠭῅").format(data)
      else:
        raise bstack1lll11l_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡪࡪࡺࡣࡩࠢࡳࡩࡷࡩࡹࠡࡶࡲ࡯ࡪࡴࠬࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡷࡹࡧࡴࡶࡵࠣ࠱ࠥࢁࡽ࠭ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨࠤࡇࡵࡤࡺࠢ࠰ࠤࢀࢃࠢῆ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack1lll11l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡࡲࡵࡳ࡯࡫ࡣࡵࠤῇ").format(e))
  def bstack11111111l1l_opy_(self):
    bstack1lllll1l1lll_opy_ = os.path.join(tempfile.gettempdir(), bstack1lll11l_opy_ (u"ࠤࡳࡩࡷࡩࡹࡄࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠧῈ"))
    try:
      if bstack1lll11l_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫΈ") not in self.bstack1lllllll1l1l_opy_:
        self.bstack1lllllll1l1l_opy_[bstack1lll11l_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬῊ")] = 2
      with open(bstack1lllll1l1lll_opy_, bstack1lll11l_opy_ (u"ࠬࡽࠧΉ")) as fp:
        json.dump(self.bstack1lllllll1l1l_opy_, fp)
      return bstack1lllll1l1lll_opy_
    except Exception as e:
      self.logger.error(bstack1lll11l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡦࡶࡪࡧࡴࡦࠢࡳࡩࡷࡩࡹࠡࡥࡲࡲ࡫࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨῌ").format(e))
  def bstack1llllll1ll11_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1llllll1l11l_opy_ == bstack1lll11l_opy_ (u"ࠧࡸ࡫ࡱࠫ῍"):
        bstack111111111ll_opy_ = [bstack1lll11l_opy_ (u"ࠨࡥࡰࡨ࠳࡫ࡸࡦࠩ῎"), bstack1lll11l_opy_ (u"ࠩ࠲ࡧࠬ῏")]
        cmd = bstack111111111ll_opy_ + cmd
      cmd = bstack1lll11l_opy_ (u"ࠪࠤࠬῐ").join(cmd)
      self.logger.debug(bstack1lll11l_opy_ (u"ࠦࡗࡻ࡮࡯࡫ࡱ࡫ࠥࢁࡽࠣῑ").format(cmd))
      with open(self.bstack1llllll1l1ll_opy_, bstack1lll11l_opy_ (u"ࠧࡧࠢῒ")) as bstack1111111l111_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1111111l111_opy_, text=True, stderr=bstack1111111l111_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1llllllll1l1_opy_ = True
      self.logger.error(bstack1lll11l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠠࡸ࡫ࡷ࡬ࠥࡩ࡭ࡥࠢ࠰ࠤࢀࢃࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࢁࡽࠣΐ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1llllll1111l_opy_:
        self.logger.info(bstack1lll11l_opy_ (u"ࠢࡔࡶࡲࡴࡵ࡯࡮ࡨࠢࡓࡩࡷࡩࡹࠣ῔"))
        cmd = [self.binary_path, bstack1lll11l_opy_ (u"ࠣࡧࡻࡩࡨࡀࡳࡵࡱࡳࠦ῕")]
        self.bstack1llllll1ll11_opy_(cmd)
        self.bstack1llllll1111l_opy_ = False
    except Exception as e:
      self.logger.error(bstack1lll11l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡰࡲࠣࡷࡪࡹࡳࡪࡱࡱࠤࡼ࡯ࡴࡩࠢࡦࡳࡲࡳࡡ࡯ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤῖ").format(cmd, e))
  def bstack1l11ll1l1l_opy_(self):
    if not self.bstack1ll11lll1l_opy_:
      return
    try:
      bstack1lllllll1ll1_opy_ = 0
      while not self.bstack1llllll1111l_opy_ and bstack1lllllll1ll1_opy_ < self.bstack11111111ll1_opy_:
        if self.bstack1llllllll1l1_opy_:
          self.logger.info(bstack1lll11l_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡶࡩࡹࡻࡰࠡࡨࡤ࡭ࡱ࡫ࡤࠣῗ"))
          return
        time.sleep(1)
        bstack1lllllll1ll1_opy_ += 1
      os.environ[bstack1lll11l_opy_ (u"ࠫࡕࡋࡒࡄ࡛ࡢࡆࡊ࡙ࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࠪῘ")] = str(self.bstack1lllll1l111l_opy_())
      self.logger.info(bstack1lll11l_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡸ࡫ࡴࡶࡲࠣࡧࡴࡳࡰ࡭ࡧࡷࡩࡩࠨῙ"))
    except Exception as e:
      self.logger.error(bstack1lll11l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡩࡹࡻࡰࠡࡲࡨࡶࡨࡿࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢῚ").format(e))
  def bstack1lllll1l111l_opy_(self):
    if self.bstack1l1ll1lll_opy_:
      return
    try:
      bstack1llllllll11l_opy_ = [platform[bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬΊ")].lower() for platform in self.config.get(bstack1lll11l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ῜"), [])]
      bstack1lllllll1111_opy_ = sys.maxsize
      bstack1lllll1l11l1_opy_ = bstack1lll11l_opy_ (u"ࠩࠪ῝")
      for browser in bstack1llllllll11l_opy_:
        if browser in self.bstack1llllll1llll_opy_:
          bstack1llllll11lll_opy_ = self.bstack1llllll1llll_opy_[browser]
        if bstack1llllll11lll_opy_ < bstack1lllllll1111_opy_:
          bstack1lllllll1111_opy_ = bstack1llllll11lll_opy_
          bstack1lllll1l11l1_opy_ = browser
      return bstack1lllll1l11l1_opy_
    except Exception as e:
      self.logger.error(bstack1lll11l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡪࡰࡧࠤࡧ࡫ࡳࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦ῞").format(e))
  @classmethod
  def bstack1ll1111ll1_opy_(self):
    return os.getenv(bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࠩ῟"), bstack1lll11l_opy_ (u"ࠬࡌࡡ࡭ࡵࡨࠫῠ")).lower()
  @classmethod
  def bstack11lllll11_opy_(self):
    return os.getenv(bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࡣࡈࡇࡐࡕࡗࡕࡉࡤࡓࡏࡅࡇࠪῡ"), bstack1lll11l_opy_ (u"ࠧࠨῢ"))
  @classmethod
  def bstack11llll1llll_opy_(cls, value):
    cls.bstack11l1111l1l_opy_ = value
  @classmethod
  def bstack1lllll1llll1_opy_(cls):
    return cls.bstack11l1111l1l_opy_
  @classmethod
  def bstack11llll1ll11_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack1llllll11111_opy_(cls):
    return cls.percy_build_id