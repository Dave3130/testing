# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
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
from bstack_utils.helper import bstack1l1llllll_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack111111ll11_opy_ import bstack1l1lll1l11_opy_
class bstack11lll11l11_opy_:
  working_dir = os.getcwd()
  bstack1l1lll11ll_opy_ = False
  config = {}
  bstack1111l1llll1_opy_ = bstack11ll1l_opy_ (u"ࠨࠩὥ")
  binary_path = bstack11ll1l_opy_ (u"ࠩࠪὦ")
  bstack1llllll111ll_opy_ = bstack11ll1l_opy_ (u"ࠪࠫὧ")
  bstack1l11l1l11_opy_ = False
  bstack1llllll11l11_opy_ = None
  bstack1lllll11ll11_opy_ = {}
  bstack11111111111_opy_ = 300
  bstack1llllll1ll11_opy_ = False
  logger = None
  bstack1lllll11l11l_opy_ = False
  bstack11ll1l11l_opy_ = False
  percy_build_id = None
  bstack1lllll1l1ll1_opy_ = bstack11ll1l_opy_ (u"ࠫࠬὨ")
  bstack1lllll1ll1ll_opy_ = {
    bstack11ll1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬὩ") : 1,
    bstack11ll1l_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࠧὪ") : 2,
    bstack11ll1l_opy_ (u"ࠧࡦࡦࡪࡩࠬὫ") : 3,
    bstack11ll1l_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨὬ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1111111111l_opy_(self):
    bstack1llllllll1ll_opy_ = bstack11ll1l_opy_ (u"ࠩࠪὭ")
    bstack1111111l1l1_opy_ = sys.platform
    bstack1lllll1l1lll_opy_ = bstack11ll1l_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩὮ")
    if re.match(bstack11ll1l_opy_ (u"ࠦࡩࡧࡲࡸ࡫ࡱࢀࡲࡧࡣࠡࡱࡶࠦὯ"), bstack1111111l1l1_opy_) != None:
      bstack1llllllll1ll_opy_ = bstack11l11l1l1ll_opy_ + bstack11ll1l_opy_ (u"ࠧ࠵ࡰࡦࡴࡦࡽ࠲ࡵࡳࡹ࠰ࡽ࡭ࡵࠨὰ")
      self.bstack1lllll1l1ll1_opy_ = bstack11ll1l_opy_ (u"࠭࡭ࡢࡥࠪά")
    elif re.match(bstack11ll1l_opy_ (u"ࠢ࡮ࡵࡺ࡭ࡳࢂ࡭ࡴࡻࡶࢀࡲ࡯࡮ࡨࡹࡿࡧࡾ࡭ࡷࡪࡰࡿࡦࡨࡩࡷࡪࡰࡿࡻ࡮ࡴࡣࡦࡾࡨࡱࡨࢂࡷࡪࡰ࠶࠶ࠧὲ"), bstack1111111l1l1_opy_) != None:
      bstack1llllllll1ll_opy_ = bstack11l11l1l1ll_opy_ + bstack11ll1l_opy_ (u"ࠣ࠱ࡳࡩࡷࡩࡹ࠮ࡹ࡬ࡲ࠳ࢀࡩࡱࠤέ")
      bstack1lllll1l1lll_opy_ = bstack11ll1l_opy_ (u"ࠤࡳࡩࡷࡩࡹ࠯ࡧࡻࡩࠧὴ")
      self.bstack1lllll1l1ll1_opy_ = bstack11ll1l_opy_ (u"ࠪࡻ࡮ࡴࠧή")
    else:
      bstack1llllllll1ll_opy_ = bstack11l11l1l1ll_opy_ + bstack11ll1l_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠱ࡱ࡯࡮ࡶࡺ࠱ࡾ࡮ࡶࠢὶ")
      self.bstack1lllll1l1ll1_opy_ = bstack11ll1l_opy_ (u"ࠬࡲࡩ࡯ࡷࡻࠫί")
    return bstack1llllllll1ll_opy_, bstack1lllll1l1lll_opy_
  def bstack1lllll11ll1l_opy_(self):
    try:
      bstack1lllll1ll111_opy_ = [os.path.join(expanduser(bstack11ll1l_opy_ (u"ࠨࡾࠣὸ")), bstack11ll1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧό")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1lllll1ll111_opy_:
        if(self.bstack1llllll1lll1_opy_(path)):
          return path
      raise bstack11ll1l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠧὺ")
    except Exception as e:
      self.logger.error(bstack11ll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪࠦࡰࡢࡶ࡫ࠤ࡫ࡵࡲࠡࡲࡨࡶࡨࡿࠠࡥࡱࡺࡲࡱࡵࡡࡥ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦ࠭ࠡࡽࢀࠦύ").format(e))
  def bstack1llllll1lll1_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1lllllll111l_opy_(self, bstack11111111l11_opy_):
    return os.path.join(bstack11111111l11_opy_, self.bstack1111l1llll1_opy_ + bstack11ll1l_opy_ (u"ࠥ࠲ࡪࡺࡡࡨࠤὼ"))
  def bstack1111111l111_opy_(self, bstack11111111l11_opy_, bstack1lllll1l1l1l_opy_):
    if not bstack1lllll1l1l1l_opy_: return
    try:
      bstack1lllll1l11l1_opy_ = self.bstack1lllllll111l_opy_(bstack11111111l11_opy_)
      with open(bstack1lllll1l11l1_opy_, bstack11ll1l_opy_ (u"ࠦࡼࠨώ")) as f:
        f.write(bstack1lllll1l1l1l_opy_)
        self.logger.debug(bstack11ll1l_opy_ (u"࡙ࠧࡡࡷࡧࡧࠤࡳ࡫ࡷࠡࡇࡗࡥ࡬ࠦࡦࡰࡴࠣࡴࡪࡸࡣࡺࠤ὾"))
    except Exception as e:
      self.logger.error(bstack11ll1l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡥࡻ࡫ࠠࡵࡪࡨࠤࡪࡺࡡࡨ࠮ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨ὿").format(e))
  def bstack1llllll1l1l1_opy_(self, bstack11111111l11_opy_):
    try:
      bstack1lllll1l11l1_opy_ = self.bstack1lllllll111l_opy_(bstack11111111l11_opy_)
      if os.path.exists(bstack1lllll1l11l1_opy_):
        with open(bstack1lllll1l11l1_opy_, bstack11ll1l_opy_ (u"ࠢࡳࠤᾀ")) as f:
          bstack1lllll1l1l1l_opy_ = f.read().strip()
          return bstack1lllll1l1l1l_opy_ if bstack1lllll1l1l1l_opy_ else None
    except Exception as e:
      self.logger.error(bstack11ll1l_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡ࡮ࡲࡥࡩ࡯࡮ࡨࠢࡈࡘࡦ࡭ࠬࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠦᾁ").format(e))
  def bstack1llllll1111l_opy_(self, bstack11111111l11_opy_, bstack1llllllll1ll_opy_):
    bstack1llllllll111_opy_ = self.bstack1llllll1l1l1_opy_(bstack11111111l11_opy_)
    if bstack1llllllll111_opy_:
      try:
        bstack1lllll1lll1l_opy_ = self.bstack1llllllll11l_opy_(bstack1llllllll111_opy_, bstack1llllllll1ll_opy_)
        if not bstack1lllll1lll1l_opy_:
          self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡ࡫ࡶࠤࡺࡶࠠࡵࡱࠣࡨࡦࡺࡥࠡࠪࡈࡘࡦ࡭ࠠࡶࡰࡦ࡬ࡦࡴࡧࡦࡦࠬࠦᾂ"))
          return True
        self.logger.debug(bstack11ll1l_opy_ (u"ࠥࡒࡪࡽࠠࡑࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡸࡴࡩࡧࡴࡦࠤᾃ"))
        return False
      except Exception as e:
        self.logger.warn(bstack11ll1l_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡤࡪࡨࡧࡰࠦࡦࡰࡴࠣࡦ࡮ࡴࡡࡳࡻࠣࡹࡵࡪࡡࡵࡧࡶ࠰ࠥࡻࡳࡪࡰࡪࠤࡪࡾࡩࡴࡶ࡬ࡲ࡬ࠦࡢࡪࡰࡤࡶࡾࡀࠠࡼࡿࠥᾄ").format(e))
    return False
  def bstack1llllllll11l_opy_(self, bstack1llllllll111_opy_, bstack1llllllll1ll_opy_):
    try:
      headers = {
        bstack11ll1l_opy_ (u"ࠧࡏࡦ࠮ࡐࡲࡲࡪ࠳ࡍࡢࡶࡦ࡬ࠧᾅ"): bstack1llllllll111_opy_
      }
      response = bstack1l1llllll_opy_(bstack11ll1l_opy_ (u"࠭ࡇࡆࡖࠪᾆ"), bstack1llllllll1ll_opy_, {}, {bstack11ll1l_opy_ (u"ࠢࡩࡧࡤࡨࡪࡸࡳࠣᾇ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack11ll1l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡤࡪࡨࡧࡰ࡯࡮ࡨࠢࡩࡳࡷࠦࡐࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡻࡰࡥࡣࡷࡩࡸࡀࠠࡼࡿࠥᾈ").format(e))
  @measure(event_name=EVENTS.bstack11l1l11l11l_opy_, stage=STAGE.bstack11ll11lll_opy_)
  def bstack1lllll1l1111_opy_(self, bstack1llllllll1ll_opy_, bstack1lllll1l1lll_opy_):
    try:
      bstack1lllll11lll1_opy_ = self.bstack1lllll11ll1l_opy_()
      bstack1llllll11l1l_opy_ = os.path.join(bstack1lllll11lll1_opy_, bstack11ll1l_opy_ (u"ࠩࡳࡩࡷࡩࡹ࠯ࡼ࡬ࡴࠬᾉ"))
      bstack1llllll1l1ll_opy_ = os.path.join(bstack1lllll11lll1_opy_, bstack1lllll1l1lll_opy_)
      if self.bstack1llllll1111l_opy_(bstack1lllll11lll1_opy_, bstack1llllllll1ll_opy_): # if bstack1llllll1l111_opy_, bstack1llllllll1l_opy_ bstack1lllll1l1l1l_opy_ is bstack1lllll1lll11_opy_ to bstack1111lll1111_opy_ version available (response 304)
        if os.path.exists(bstack1llllll1l1ll_opy_):
          self.logger.info(bstack11ll1l_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࢀࢃࠬࠡࡵ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠧᾊ").format(bstack1llllll1l1ll_opy_))
          return bstack1llllll1l1ll_opy_
        if os.path.exists(bstack1llllll11l1l_opy_):
          self.logger.info(bstack11ll1l_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡾ࡮ࡶࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡾࢁ࠱ࠦࡵ࡯ࡼ࡬ࡴࡵ࡯࡮ࡨࠤᾋ").format(bstack1llllll11l1l_opy_))
          return self.bstack1llllllllll1_opy_(bstack1llllll11l1l_opy_, bstack1lllll1l1lll_opy_)
      self.logger.info(bstack11ll1l_opy_ (u"ࠧࡊ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡶࡴࡳࠠࡼࡿࠥᾌ").format(bstack1llllllll1ll_opy_))
      response = bstack1l1llllll_opy_(bstack11ll1l_opy_ (u"࠭ࡇࡆࡖࠪᾍ"), bstack1llllllll1ll_opy_, {}, {})
      if response.status_code == 200:
        bstack1lllllllll1l_opy_ = response.headers.get(bstack11ll1l_opy_ (u"ࠢࡆࡖࡤ࡫ࠧᾎ"), bstack11ll1l_opy_ (u"ࠣࠤᾏ"))
        if bstack1lllllllll1l_opy_:
          self.bstack1111111l111_opy_(bstack1lllll11lll1_opy_, bstack1lllllllll1l_opy_)
        with open(bstack1llllll11l1l_opy_, bstack11ll1l_opy_ (u"ࠩࡺࡦࠬᾐ")) as file:
          file.write(response.content)
        self.logger.info(bstack11ll1l_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡡ࡯ࡦࠣࡷࡦࡼࡥࡥࠢࡤࡸࠥࢁࡽࠣᾑ").format(bstack1llllll11l1l_opy_))
        return self.bstack1llllllllll1_opy_(bstack1llllll11l1l_opy_, bstack1lllll1l1lll_opy_)
      else:
        raise(bstack11ll1l_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡷ࡬ࡪࠦࡦࡪ࡮ࡨ࠲࡙ࠥࡴࡢࡶࡸࡷࠥࡩ࡯ࡥࡧ࠽ࠤࢀࢃࠢᾒ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack11ll1l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺ࠼ࠣࡿࢂࠨᾓ").format(e))
  def bstack1llllll111l1_opy_(self, bstack1llllllll1ll_opy_, bstack1lllll1l1lll_opy_):
    try:
      retry = 2
      bstack1llllll1l1ll_opy_ = None
      bstack1llllll1ll1l_opy_ = False
      while retry > 0:
        bstack1llllll1l1ll_opy_ = self.bstack1lllll1l1111_opy_(bstack1llllllll1ll_opy_, bstack1lllll1l1lll_opy_)
        bstack1llllll1ll1l_opy_ = self.bstack11111111lll_opy_(bstack1llllllll1ll_opy_, bstack1lllll1l1lll_opy_, bstack1llllll1l1ll_opy_)
        if bstack1llllll1ll1l_opy_:
          break
        retry -= 1
      return bstack1llllll1l1ll_opy_, bstack1llllll1ll1l_opy_
    except Exception as e:
      self.logger.error(bstack11ll1l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡪࡩࡹࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡶࡡࡵࡪࠥᾔ").format(e))
    return bstack1llllll1l1ll_opy_, False
  def bstack11111111lll_opy_(self, bstack1llllllll1ll_opy_, bstack1lllll1l1lll_opy_, bstack1llllll1l1ll_opy_, bstack11111111l1l_opy_ = 0):
    if bstack11111111l1l_opy_ > 1:
      return False
    if bstack1llllll1l1ll_opy_ == None or os.path.exists(bstack1llllll1l1ll_opy_) == False:
      self.logger.warn(bstack11ll1l_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡰࡢࡶ࡫ࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠬࠡࡴࡨࡸࡷࡿࡩ࡯ࡩࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠧᾕ"))
      return False
    bstack1lllll1ll11l_opy_ = bstack11ll1l_opy_ (u"ࡳࠤࡡ࠲࠯ࡆࡰࡦࡴࡦࡽ࠴ࡩ࡬ࡪࠢ࡟ࡨ࠰ࡢ࠮࡝ࡦ࠮ࡠ࠳ࡢࡤࠬࠤᾖ")
    command = bstack11ll1l_opy_ (u"ࠩࡾࢁࠥ࠳࠭ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᾗ").format(bstack1llllll1l1ll_opy_)
    bstack1llllll1l11l_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1lllll1ll11l_opy_, bstack1llllll1l11l_opy_) != None:
      return True
    else:
      self.logger.error(bstack11ll1l_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡹࡩࡷࡹࡩࡰࡰࠣࡧ࡭࡫ࡣ࡬ࠢࡩࡥ࡮ࡲࡥࡥࠤᾘ"))
      return False
  def bstack1llllllllll1_opy_(self, bstack1llllll11l1l_opy_, bstack1lllll1l1lll_opy_):
    try:
      working_dir = os.path.dirname(bstack1llllll11l1l_opy_)
      shutil.unpack_archive(bstack1llllll11l1l_opy_, working_dir)
      bstack1llllll1l1ll_opy_ = os.path.join(working_dir, bstack1lllll1l1lll_opy_)
      os.chmod(bstack1llllll1l1ll_opy_, 0o755)
      return bstack1llllll1l1ll_opy_
    except Exception as e:
      self.logger.error(bstack11ll1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡶࡰࡽ࡭ࡵࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠧᾙ"))
  def bstack1lllllll1ll1_opy_(self):
    try:
      bstack1111111l11l_opy_ = self.config.get(bstack11ll1l_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫᾚ"))
      bstack1lllllll1ll1_opy_ = bstack1111111l11l_opy_ or (bstack1111111l11l_opy_ is None and self.bstack1l1lll11ll_opy_)
      if not bstack1lllllll1ll1_opy_ or self.config.get(bstack11ll1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩᾛ"), None) not in bstack11l11l11lll_opy_:
        return False
      self.bstack1l11l1l11_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack11ll1l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡪࡺࡥࡤࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᾜ").format(e))
  def bstack1lllll1lllll_opy_(self):
    try:
      bstack1lllll1lllll_opy_ = self.percy_capture_mode
      return bstack1lllll1lllll_opy_
    except Exception as e:
      self.logger.error(bstack11ll1l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩ࡫ࡴࡦࡥࡷࠤࡵ࡫ࡲࡤࡻࠣࡧࡦࡶࡴࡶࡴࡨࠤࡲࡵࡤࡦ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᾝ").format(e))
  def init(self, bstack1l1lll11ll_opy_, config, logger):
    self.bstack1l1lll11ll_opy_ = bstack1l1lll11ll_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1lllllll1ll1_opy_():
      return
    self.bstack1lllll11ll11_opy_ = config.get(bstack11ll1l_opy_ (u"ࠩࡳࡩࡷࡩࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᾞ"), {})
    self.percy_capture_mode = config.get(bstack11ll1l_opy_ (u"ࠪࡴࡪࡸࡣࡺࡅࡤࡴࡹࡻࡲࡦࡏࡲࡨࡪ࠭ᾟ"))
    try:
      bstack1llllllll1ll_opy_, bstack1lllll1l1lll_opy_ = self.bstack1111111111l_opy_()
      self.bstack1111l1llll1_opy_ = bstack1lllll1l1lll_opy_
      bstack1llllll1l1ll_opy_, bstack1llllll1ll1l_opy_ = self.bstack1llllll111l1_opy_(bstack1llllllll1ll_opy_, bstack1lllll1l1lll_opy_)
      if bstack1llllll1ll1l_opy_:
        self.binary_path = bstack1llllll1l1ll_opy_
        thread = Thread(target=self.bstack1lllll11l1l1_opy_)
        thread.start()
      else:
        self.bstack1lllll11l11l_opy_ = True
        self.logger.error(bstack11ll1l_opy_ (u"ࠦࡎࡴࡶࡢ࡮࡬ࡨࠥࡶࡥࡳࡥࡼࠤࡵࡧࡴࡩࠢࡩࡳࡺࡴࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡓࡩࡷࡩࡹࠣᾠ").format(bstack1llllll1l1ll_opy_))
    except Exception as e:
      self.logger.error(bstack11ll1l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᾡ").format(e))
  def bstack1lllllll1l1l_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack11ll1l_opy_ (u"࠭࡬ࡰࡩࠪᾢ"), bstack11ll1l_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠴࡬ࡰࡩࠪᾣ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack11ll1l_opy_ (u"ࠣࡒࡸࡷ࡭࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡ࡮ࡲ࡫ࡸࠦࡡࡵࠢࡾࢁࠧᾤ").format(logfile))
      self.bstack1llllll111ll_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack11ll1l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡥࡵࠢࡳࡩࡷࡩࡹࠡ࡮ࡲ࡫ࠥࡶࡡࡵࡪ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥᾥ").format(e))
  @measure(event_name=EVENTS.bstack11l1l111lll_opy_, stage=STAGE.bstack11ll11lll_opy_)
  def bstack1lllll11l1l1_opy_(self):
    bstack1llllllll1l1_opy_ = self.bstack1lllll1ll1l1_opy_()
    if bstack1llllllll1l1_opy_ == None:
      self.bstack1lllll11l11l_opy_ = True
      self.logger.error(bstack11ll1l_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡷࡳࡰ࡫࡮ࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧ࠰ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾࠨᾦ"))
      return False
    bstack11111111ll1_opy_ = [bstack11ll1l_opy_ (u"ࠦࡦࡶࡰ࠻ࡧࡻࡩࡨࡀࡳࡵࡣࡵࡸࠧᾧ") if self.bstack1l1lll11ll_opy_ else bstack11ll1l_opy_ (u"ࠬ࡫ࡸࡦࡥ࠽ࡷࡹࡧࡲࡵࠩᾨ")]
    bstack11111ll111l_opy_ = self.bstack1lllllll1111_opy_()
    if bstack11111ll111l_opy_ != None:
      bstack11111111ll1_opy_.append(bstack11ll1l_opy_ (u"ࠨ࠭ࡤࠢࡾࢁࠧᾩ").format(bstack11111ll111l_opy_))
    env = os.environ.copy()
    env[bstack11ll1l_opy_ (u"ࠢࡑࡇࡕࡇ࡞ࡥࡔࡐࡍࡈࡒࠧᾪ")] = bstack1llllllll1l1_opy_
    env[bstack11ll1l_opy_ (u"ࠣࡖࡋࡣࡇ࡛ࡉࡍࡆࡢ࡙࡚ࡏࡄࠣᾫ")] = os.environ.get(bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᾬ"), bstack11ll1l_opy_ (u"ࠪࠫᾭ"))
    bstack1lllllll1lll_opy_ = [self.binary_path]
    self.bstack1lllllll1l1l_opy_()
    self.bstack1llllll11l11_opy_ = self.bstack1lllllll11ll_opy_(bstack1lllllll1lll_opy_ + bstack11111111ll1_opy_, env)
    self.logger.debug(bstack11ll1l_opy_ (u"ࠦࡘࡺࡡࡳࡶ࡬ࡲ࡬ࠦࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠧᾮ"))
    bstack11111111l1l_opy_ = 0
    while self.bstack1llllll11l11_opy_.poll() == None:
      bstack1lllllllllll_opy_ = self.bstack1llllll11lll_opy_()
      if bstack1lllllllllll_opy_:
        self.logger.debug(bstack11ll1l_opy_ (u"ࠧࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠤࡸࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬ࠣᾯ"))
        self.bstack1llllll1ll11_opy_ = True
        return True
      bstack11111111l1l_opy_ += 1
      self.logger.debug(bstack11ll1l_opy_ (u"ࠨࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡘࡥࡵࡴࡼࠤ࠲ࠦࡻࡾࠤᾰ").format(bstack11111111l1l_opy_))
      time.sleep(2)
    self.logger.error(bstack11ll1l_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡣࡩࡸࡪࡸࠠࡼࡿࠣࡥࡹࡺࡥ࡮ࡲࡷࡷࠧᾱ").format(bstack11111111l1l_opy_))
    self.bstack1lllll11l11l_opy_ = True
    return False
  def bstack1llllll11lll_opy_(self, bstack11111111l1l_opy_ = 0):
    if bstack11111111l1l_opy_ > 10:
      return False
    try:
      bstack1llllll1llll_opy_ = os.environ.get(bstack11ll1l_opy_ (u"ࠨࡒࡈࡖࡈ࡟࡟ࡔࡇࡕ࡚ࡊࡘ࡟ࡂࡆࡇࡖࡊ࡙ࡓࠨᾲ"), bstack11ll1l_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱࡯ࡳࡨࡧ࡬ࡩࡱࡶࡸ࠿࠻࠳࠴࠺ࠪᾳ"))
      bstack1lllll11l1ll_opy_ = bstack1llllll1llll_opy_ + bstack11l11l1ll11_opy_
      response = requests.get(bstack1lllll11l1ll_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack11ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࠩᾴ"), {}).get(bstack11ll1l_opy_ (u"ࠫ࡮ࡪࠧ᾵"), None)
      return True
    except:
      self.logger.debug(bstack11ll1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡴࡩࡣࡶࡴࡵࡩࡩࠦࡷࡩ࡫࡯ࡩࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡲࡴࡩࠢࡦ࡬ࡪࡩ࡫ࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࠥᾶ"))
      return False
  def bstack1lllll1ll1l1_opy_(self):
    bstack1lllllll1l11_opy_ = bstack11ll1l_opy_ (u"࠭ࡡࡱࡲࠪᾷ") if self.bstack1l1lll11ll_opy_ else bstack11ll1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩᾸ")
    bstack1lllll1l1l11_opy_ = bstack11ll1l_opy_ (u"ࠣࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧࠦᾹ") if self.config.get(bstack11ll1l_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨᾺ")) is None else True
    bstack11ll111l11l_opy_ = bstack11ll1l_opy_ (u"ࠥࡥࡵ࡯࠯ࡢࡲࡳࡣࡵ࡫ࡲࡤࡻ࠲࡫ࡪࡺ࡟ࡱࡴࡲ࡮ࡪࡩࡴࡠࡶࡲ࡯ࡪࡴ࠿࡯ࡣࡰࡩࡂࢁࡽࠧࡶࡼࡴࡪࡃࡻࡾࠨࡳࡩࡷࡩࡹ࠾ࡽࢀࠦΆ").format(self.config[bstack11ll1l_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᾼ")], bstack1lllllll1l11_opy_, bstack1lllll1l1l11_opy_)
    if self.percy_capture_mode:
      bstack11ll111l11l_opy_ += bstack11ll1l_opy_ (u"ࠧࠬࡰࡦࡴࡦࡽࡤࡩࡡࡱࡶࡸࡶࡪࡥ࡭ࡰࡦࡨࡁࢀࢃࠢ᾽").format(self.percy_capture_mode)
    uri = bstack1l1lll1l11_opy_(bstack11ll111l11l_opy_)
    try:
      response = bstack1l1llllll_opy_(bstack11ll1l_opy_ (u"࠭ࡇࡆࡖࠪι"), uri, {}, {bstack11ll1l_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ᾿"): (self.config[bstack11ll1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ῀")], self.config[bstack11ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ῁")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack1l11l1l11_opy_ = data.get(bstack11ll1l_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫῂ"))
        self.percy_capture_mode = data.get(bstack11ll1l_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡢࡧࡦࡶࡴࡶࡴࡨࡣࡲࡵࡤࡦࠩῃ"))
        os.environ[bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࠪῄ")] = str(self.bstack1l11l1l11_opy_)
        os.environ[bstack11ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࡣࡈࡇࡐࡕࡗࡕࡉࡤࡓࡏࡅࡇࠪ῅")] = str(self.percy_capture_mode)
        if bstack1lllll1l1l11_opy_ == bstack11ll1l_opy_ (u"ࠢࡶࡰࡧࡩ࡫࡯࡮ࡦࡦࠥῆ") and str(self.bstack1l11l1l11_opy_).lower() == bstack11ll1l_opy_ (u"ࠣࡶࡵࡹࡪࠨῇ"):
          self.bstack11ll1l11l_opy_ = True
        if bstack11ll1l_opy_ (u"ࠤࡷࡳࡰ࡫࡮ࠣῈ") in data:
          return data[bstack11ll1l_opy_ (u"ࠥࡸࡴࡱࡥ࡯ࠤΈ")]
        else:
          raise bstack11ll1l_opy_ (u"࡙ࠫࡵ࡫ࡦࡰࠣࡒࡴࡺࠠࡇࡱࡸࡲࡩࠦ࠭ࠡࡽࢀࠫῊ").format(data)
      else:
        raise bstack11ll1l_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡨࡨࡸࡨ࡮ࠠࡱࡧࡵࡧࡾࠦࡴࡰ࡭ࡨࡲ࠱ࠦࡒࡦࡵࡳࡳࡳࡹࡥࠡࡵࡷࡥࡹࡻࡳࠡ࠯ࠣࡿࢂ࠲ࠠࡓࡧࡶࡴࡴࡴࡳࡦࠢࡅࡳࡩࡿࠠ࠮ࠢࡾࢁࠧΉ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack11ll1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡱࡧࡵࡧࡾࠦࡰࡳࡱ࡭ࡩࡨࡺࠢῌ").format(e))
  def bstack1lllllll1111_opy_(self):
    bstack111111111ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1l_opy_ (u"ࠢࡱࡧࡵࡧࡾࡉ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠥ῍"))
    try:
      if bstack11ll1l_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩ῎") not in self.bstack1lllll11ll11_opy_:
        self.bstack1lllll11ll11_opy_[bstack11ll1l_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪ῏")] = 2
      with open(bstack111111111ll_opy_, bstack11ll1l_opy_ (u"ࠪࡻࠬῐ")) as fp:
        json.dump(self.bstack1lllll11ll11_opy_, fp)
      return bstack111111111ll_opy_
    except Exception as e:
      self.logger.error(bstack11ll1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡤࡴࡨࡥࡹ࡫ࠠࡱࡧࡵࡧࡾࠦࡣࡰࡰࡩ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦῑ").format(e))
  def bstack1lllllll11ll_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1lllll1l1ll1_opy_ == bstack11ll1l_opy_ (u"ࠬࡽࡩ࡯ࠩῒ"):
        bstack1lllll1llll1_opy_ = [bstack11ll1l_opy_ (u"࠭ࡣ࡮ࡦ࠱ࡩࡽ࡫ࠧΐ"), bstack11ll1l_opy_ (u"ࠧ࠰ࡥࠪ῔")]
        cmd = bstack1lllll1llll1_opy_ + cmd
      cmd = bstack11ll1l_opy_ (u"ࠨࠢࠪ῕").join(cmd)
      self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡕࡹࡳࡴࡩ࡯ࡩࠣࡿࢂࠨῖ").format(cmd))
      with open(self.bstack1llllll111ll_opy_, bstack11ll1l_opy_ (u"ࠥࡥࠧῗ")) as bstack111111111l1_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack111111111l1_opy_, text=True, stderr=bstack111111111l1_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1lllll11l11l_opy_ = True
      self.logger.error(bstack11ll1l_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽࠥࡽࡩࡵࡪࠣࡧࡲࡪࠠ࠮ࠢࡾࢁ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࡿࢂࠨῘ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1llllll1ll11_opy_:
        self.logger.info(bstack11ll1l_opy_ (u"࡙ࠧࡴࡰࡲࡳ࡭ࡳ࡭ࠠࡑࡧࡵࡧࡾࠨῙ"))
        cmd = [self.binary_path, bstack11ll1l_opy_ (u"ࠨࡥࡹࡧࡦ࠾ࡸࡺ࡯ࡱࠤῚ")]
        self.bstack1lllllll11ll_opy_(cmd)
        self.bstack1llllll1ll11_opy_ = False
    except Exception as e:
      self.logger.error(bstack11ll1l_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡵࡰࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡺ࡭ࡹ࡮ࠠࡤࡱࡰࡱࡦࡴࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃࠢΊ").format(cmd, e))
  def bstack1l1111lll1_opy_(self):
    if not self.bstack1l11l1l11_opy_:
      return
    try:
      bstack1111111l1ll_opy_ = 0
      while not self.bstack1llllll1ll11_opy_ and bstack1111111l1ll_opy_ < self.bstack11111111111_opy_:
        if self.bstack1lllll11l11l_opy_:
          self.logger.info(bstack11ll1l_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡴࡧࡷࡹࡵࠦࡦࡢ࡫࡯ࡩࡩࠨ῜"))
          return
        time.sleep(1)
        bstack1111111l1ll_opy_ += 1
      os.environ[bstack11ll1l_opy_ (u"ࠩࡓࡉࡗࡉ࡙ࡠࡄࡈࡗ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࠨ῝")] = str(self.bstack1llllll11111_opy_())
      self.logger.info(bstack11ll1l_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡶࡩࡹࡻࡰࠡࡥࡲࡱࡵࡲࡥࡵࡧࡧࠦ῞"))
    except Exception as e:
      self.logger.error(bstack11ll1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡧࡷࡹࡵࠦࡰࡦࡴࡦࡽ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧ῟").format(e))
  def bstack1llllll11111_opy_(self):
    if self.bstack1l1lll11ll_opy_:
      return
    try:
      bstack1lllllll11l1_opy_ = [platform[bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪῠ")].lower() for platform in self.config.get(bstack11ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩῡ"), [])]
      bstack1lllll11llll_opy_ = sys.maxsize
      bstack1llllll11ll1_opy_ = bstack11ll1l_opy_ (u"ࠧࠨῢ")
      for browser in bstack1lllllll11l1_opy_:
        if browser in self.bstack1lllll1ll1ll_opy_:
          bstack1lllllllll11_opy_ = self.bstack1lllll1ll1ll_opy_[browser]
        if bstack1lllllllll11_opy_ < bstack1lllll11llll_opy_:
          bstack1lllll11llll_opy_ = bstack1lllllllll11_opy_
          bstack1llllll11ll1_opy_ = browser
      return bstack1llllll11ll1_opy_
    except Exception as e:
      self.logger.error(bstack11ll1l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡥࡩࡸࡺࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤΰ").format(e))
  @classmethod
  def bstack1l1l11111_opy_(self):
    return os.getenv(bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟ࠧῤ"), bstack11ll1l_opy_ (u"ࠪࡊࡦࡲࡳࡦࠩῥ")).lower()
  @classmethod
  def bstack11l1l1111l_opy_(self):
    return os.getenv(bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࡡࡆࡅࡕ࡚ࡕࡓࡇࡢࡑࡔࡊࡅࠨῦ"), bstack11ll1l_opy_ (u"ࠬ࠭ῧ"))
  @classmethod
  def bstack11lllll11l1_opy_(cls, value):
    cls.bstack11ll1l11l_opy_ = value
  @classmethod
  def bstack1lllll1l11ll_opy_(cls):
    return cls.bstack11ll1l11l_opy_
  @classmethod
  def bstack11lllll1111_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack1lllll1l111l_opy_(cls):
    return cls.percy_build_id