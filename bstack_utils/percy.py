# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
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
from bstack_utils.helper import bstack11ll11ll1l_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l111l11l_opy_ import bstack11ll1l1l1_opy_
class bstack1ll1l1ll1l_opy_:
  working_dir = os.getcwd()
  bstack11l1l1l11l_opy_ = False
  config = {}
  bstack111l1l11l11_opy_ = bstack11l111_opy_ (u"ࠧࠨ἗")
  binary_path = bstack11l111_opy_ (u"ࠨࠩἘ")
  bstack1lllll1ll1ll_opy_ = bstack11l111_opy_ (u"ࠩࠪἙ")
  bstack11l1l1ll11_opy_ = False
  bstack111111l1l11_opy_ = None
  bstack111111l1l1l_opy_ = {}
  bstack1lllll1l1lll_opy_ = 300
  bstack1llllllll1l1_opy_ = False
  logger = None
  bstack1llllll1111l_opy_ = False
  bstack11l1l1111l_opy_ = False
  percy_build_id = None
  bstack1llllll1l11l_opy_ = bstack11l111_opy_ (u"ࠪࠫἚ")
  bstack1lllllll11l1_opy_ = {
    bstack11l111_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫἛ") : 1,
    bstack11l111_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭Ἔ") : 2,
    bstack11l111_opy_ (u"࠭ࡥࡥࡩࡨࠫἝ") : 3,
    bstack11l111_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࠧ἞") : 4
  }
  def __init__(self) -> None: pass
  def bstack1lllllll1lll_opy_(self):
    bstack1111111llll_opy_ = bstack11l111_opy_ (u"ࠨࠩ἟")
    bstack1111111l11l_opy_ = sys.platform
    bstack1111111ll11_opy_ = bstack11l111_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨἠ")
    if re.match(bstack11l111_opy_ (u"ࠥࡨࡦࡸࡷࡪࡰࡿࡱࡦࡩࠠࡰࡵࠥἡ"), bstack1111111l11l_opy_) != None:
      bstack1111111llll_opy_ = bstack11l11ll11l1_opy_ + bstack11l111_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠱ࡴࡹࡸ࠯ࡼ࡬ࡴࠧἢ")
      self.bstack1llllll1l11l_opy_ = bstack11l111_opy_ (u"ࠬࡳࡡࡤࠩἣ")
    elif re.match(bstack11l111_opy_ (u"ࠨ࡭ࡴࡹ࡬ࡲࢁࡳࡳࡺࡵࡿࡱ࡮ࡴࡧࡸࡾࡦࡽ࡬ࡽࡩ࡯ࡾࡥࡧࡨࡽࡩ࡯ࡾࡺ࡭ࡳࡩࡥࡽࡧࡰࡧࢁࡽࡩ࡯࠵࠵ࠦἤ"), bstack1111111l11l_opy_) != None:
      bstack1111111llll_opy_ = bstack11l11ll11l1_opy_ + bstack11l111_opy_ (u"ࠢ࠰ࡲࡨࡶࡨࡿ࠭ࡸ࡫ࡱ࠲ࡿ࡯ࡰࠣἥ")
      bstack1111111ll11_opy_ = bstack11l111_opy_ (u"ࠣࡲࡨࡶࡨࡿ࠮ࡦࡺࡨࠦἦ")
      self.bstack1llllll1l11l_opy_ = bstack11l111_opy_ (u"ࠩࡺ࡭ࡳ࠭ἧ")
    else:
      bstack1111111llll_opy_ = bstack11l11ll11l1_opy_ + bstack11l111_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠰ࡰ࡮ࡴࡵࡹ࠰ࡽ࡭ࡵࠨἨ")
      self.bstack1llllll1l11l_opy_ = bstack11l111_opy_ (u"ࠫࡱ࡯࡮ࡶࡺࠪἩ")
    return bstack1111111llll_opy_, bstack1111111ll11_opy_
  def bstack111111l1111_opy_(self):
    try:
      bstack1lllll1l1l1l_opy_ = [os.path.join(expanduser(bstack11l111_opy_ (u"ࠧࢄࠢἪ")), bstack11l111_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭Ἣ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1lllll1l1l1l_opy_:
        if(self.bstack111111l111l_opy_(path)):
          return path
      raise bstack11l111_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠦἬ")
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩࠥࡶࡡࡵࡪࠣࡪࡴࡸࠠࡱࡧࡵࡧࡾࠦࡤࡰࡹࡱࡰࡴࡧࡤ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࠳ࠠࡼࡿࠥἭ").format(e))
  def bstack111111l111l_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1llllllll1ll_opy_(self, bstack1llllll1llll_opy_):
    return os.path.join(bstack1llllll1llll_opy_, self.bstack111l1l11l11_opy_ + bstack11l111_opy_ (u"ࠤ࠱ࡩࡹࡧࡧࠣἮ"))
  def bstack11111111l1l_opy_(self, bstack1llllll1llll_opy_, bstack1lllllllll11_opy_):
    if not bstack1lllllllll11_opy_: return
    try:
      bstack1lllll1ll11l_opy_ = self.bstack1llllllll1ll_opy_(bstack1llllll1llll_opy_)
      with open(bstack1lllll1ll11l_opy_, bstack11l111_opy_ (u"ࠥࡻࠧἯ")) as f:
        f.write(bstack1lllllllll11_opy_)
        self.logger.debug(bstack11l111_opy_ (u"ࠦࡘࡧࡶࡦࡦࠣࡲࡪࡽࠠࡆࡖࡤ࡫ࠥ࡬࡯ࡳࠢࡳࡩࡷࡩࡹࠣἰ"))
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡤࡺࡪࠦࡴࡩࡧࠣࡩࡹࡧࡧ࠭ࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠧἱ").format(e))
  def bstack1lllll1l1ll1_opy_(self, bstack1llllll1llll_opy_):
    try:
      bstack1lllll1ll11l_opy_ = self.bstack1llllllll1ll_opy_(bstack1llllll1llll_opy_)
      if os.path.exists(bstack1lllll1ll11l_opy_):
        with open(bstack1lllll1ll11l_opy_, bstack11l111_opy_ (u"ࠨࡲࠣἲ")) as f:
          bstack1lllllllll11_opy_ = f.read().strip()
          return bstack1lllllllll11_opy_ if bstack1lllllllll11_opy_ else None
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠ࡭ࡱࡤࡨ࡮ࡴࡧࠡࡇࡗࡥ࡬࠲ࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥἳ").format(e))
  def bstack1lllll1l1l11_opy_(self, bstack1llllll1llll_opy_, bstack1111111llll_opy_):
    bstack1lllllll111l_opy_ = self.bstack1lllll1l1ll1_opy_(bstack1llllll1llll_opy_)
    if bstack1lllllll111l_opy_:
      try:
        bstack1lllllllllll_opy_ = self.bstack1llllll1l111_opy_(bstack1lllllll111l_opy_, bstack1111111llll_opy_)
        if not bstack1lllllllllll_opy_:
          self.logger.debug(bstack11l111_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡪࡵࠣࡹࡵࠦࡴࡰࠢࡧࡥࡹ࡫ࠠࠩࡇࡗࡥ࡬ࠦࡵ࡯ࡥ࡫ࡥࡳ࡭ࡥࡥࠫࠥἴ"))
          return True
        self.logger.debug(bstack11l111_opy_ (u"ࠤࡑࡩࡼࠦࡐࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦ࠮ࠣࡨࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡷࡳࡨࡦࡺࡥࠣἵ"))
        return False
      except Exception as e:
        self.logger.warn(bstack11l111_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡣࡩࡧࡦ࡯ࠥ࡬࡯ࡳࠢࡥ࡭ࡳࡧࡲࡺࠢࡸࡴࡩࡧࡴࡦࡵ࠯ࠤࡺࡹࡩ࡯ࡩࠣࡩࡽ࡯ࡳࡵ࡫ࡱ࡫ࠥࡨࡩ࡯ࡣࡵࡽ࠿ࠦࡻࡾࠤἶ").format(e))
    return False
  def bstack1llllll1l111_opy_(self, bstack1lllllll111l_opy_, bstack1111111llll_opy_):
    try:
      headers = {
        bstack11l111_opy_ (u"ࠦࡎ࡬࠭ࡏࡱࡱࡩ࠲ࡓࡡࡵࡥ࡫ࠦἷ"): bstack1lllllll111l_opy_
      }
      response = bstack11ll11ll1l_opy_(bstack11l111_opy_ (u"ࠬࡍࡅࡕࠩἸ"), bstack1111111llll_opy_, {}, {bstack11l111_opy_ (u"ࠨࡨࡦࡣࡧࡩࡷࡹࠢἹ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack11l111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡣࡩࡧࡦ࡯࡮ࡴࡧࠡࡨࡲࡶࠥࡖࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤࡺࡶࡤࡢࡶࡨࡷ࠿ࠦࡻࡾࠤἺ").format(e))
  @measure(event_name=EVENTS.bstack11l1l11111l_opy_, stage=STAGE.bstack1l111l11l_opy_)
  def bstack1llllll1l1l1_opy_(self, bstack1111111llll_opy_, bstack1111111ll11_opy_):
    try:
      bstack1llllllllll1_opy_ = self.bstack111111l1111_opy_()
      bstack1lllllll1l1l_opy_ = os.path.join(bstack1llllllllll1_opy_, bstack11l111_opy_ (u"ࠨࡲࡨࡶࡨࡿ࠮ࡻ࡫ࡳࠫἻ"))
      bstack1llllll1l1ll_opy_ = os.path.join(bstack1llllllllll1_opy_, bstack1111111ll11_opy_)
      if self.bstack1lllll1l1l11_opy_(bstack1llllllllll1_opy_, bstack1111111llll_opy_): # if bstack1lllllllll1l_opy_, bstack111111l1l1_opy_ bstack1lllllllll11_opy_ is bstack111111l11ll_opy_ to bstack111l111ll1l_opy_ version available (response 304)
        if os.path.exists(bstack1llllll1l1ll_opy_):
          self.logger.info(bstack11l111_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡿࢂ࠲ࠠࡴ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠦἼ").format(bstack1llllll1l1ll_opy_))
          return bstack1llllll1l1ll_opy_
        if os.path.exists(bstack1lllllll1l1l_opy_):
          self.logger.info(bstack11l111_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡽ࡭ࡵࠦࡦࡰࡷࡱࡨࠥ࡯࡮ࠡࡽࢀ࠰ࠥࡻ࡮ࡻ࡫ࡳࡴ࡮ࡴࡧࠣἽ").format(bstack1lllllll1l1l_opy_))
          return self.bstack11111111lll_opy_(bstack1lllllll1l1l_opy_, bstack1111111ll11_opy_)
      self.logger.info(bstack11l111_opy_ (u"ࠦࡉࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡨࡵࡳࡲࠦࡻࡾࠤἾ").format(bstack1111111llll_opy_))
      response = bstack11ll11ll1l_opy_(bstack11l111_opy_ (u"ࠬࡍࡅࡕࠩἿ"), bstack1111111llll_opy_, {}, {})
      if response.status_code == 200:
        bstack1llllll111l1_opy_ = response.headers.get(bstack11l111_opy_ (u"ࠨࡅࡕࡣࡪࠦὀ"), bstack11l111_opy_ (u"ࠢࠣὁ"))
        if bstack1llllll111l1_opy_:
          self.bstack11111111l1l_opy_(bstack1llllllllll1_opy_, bstack1llllll111l1_opy_)
        with open(bstack1lllllll1l1l_opy_, bstack11l111_opy_ (u"ࠨࡹࡥࠫὂ")) as file:
          file.write(response.content)
        self.logger.info(bstack11l111_opy_ (u"ࠤࡇࡳࡼࡴ࡬ࡰࡣࡧࡩࡩࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡧ࡮ࡥࠢࡶࡥࡻ࡫ࡤࠡࡣࡷࠤࢀࢃࠢὃ").format(bstack1lllllll1l1l_opy_))
        return self.bstack11111111lll_opy_(bstack1lllllll1l1l_opy_, bstack1111111ll11_opy_)
      else:
        raise(bstack11l111_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡶ࡫ࡩࠥ࡬ࡩ࡭ࡧ࠱ࠤࡘࡺࡡࡵࡷࡶࠤࡨࡵࡤࡦ࠼ࠣࡿࢂࠨὄ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹ࠻ࠢࡾࢁࠧὅ").format(e))
  def bstack1llllll11lll_opy_(self, bstack1111111llll_opy_, bstack1111111ll11_opy_):
    try:
      retry = 2
      bstack1llllll1l1ll_opy_ = None
      bstack1llllll1lll1_opy_ = False
      while retry > 0:
        bstack1llllll1l1ll_opy_ = self.bstack1llllll1l1l1_opy_(bstack1111111llll_opy_, bstack1111111ll11_opy_)
        bstack1llllll1lll1_opy_ = self.bstack111111111l1_opy_(bstack1111111llll_opy_, bstack1111111ll11_opy_, bstack1llllll1l1ll_opy_)
        if bstack1llllll1lll1_opy_:
          break
        retry -= 1
      return bstack1llllll1l1ll_opy_, bstack1llllll1lll1_opy_
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡩࡨࡸࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤࡵࡧࡴࡩࠤ὆").format(e))
    return bstack1llllll1l1ll_opy_, False
  def bstack111111111l1_opy_(self, bstack1111111llll_opy_, bstack1111111ll11_opy_, bstack1llllll1l1ll_opy_, bstack11111111ll1_opy_ = 0):
    if bstack11111111ll1_opy_ > 1:
      return False
    if bstack1llllll1l1ll_opy_ == None or os.path.exists(bstack1llllll1l1ll_opy_) == False:
      self.logger.warn(bstack11l111_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡶࡡࡵࡪࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩ࠲ࠠࡳࡧࡷࡶࡾ࡯࡮ࡨࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠦ὇"))
      return False
    bstack1llllll11111_opy_ = bstack11l111_opy_ (u"ࡲࠣࡠ࠱࠮ࡅࡶࡥࡳࡥࡼ࠳ࡨࡲࡩࠡ࡞ࡧ࠯ࡡ࠴࡜ࡥ࠭࡟࠲ࡡࡪࠫࠣὈ")
    command = bstack11l111_opy_ (u"ࠨࡽࢀࠤ࠲࠳ࡶࡦࡴࡶ࡭ࡴࡴࠧὉ").format(bstack1llllll1l1ll_opy_)
    bstack1llllll11ll1_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1llllll11111_opy_, bstack1llllll11ll1_opy_) != None:
      return True
    else:
      self.logger.error(bstack11l111_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡦ࡬ࡪࡩ࡫ࠡࡨࡤ࡭ࡱ࡫ࡤࠣὊ"))
      return False
  def bstack11111111lll_opy_(self, bstack1lllllll1l1l_opy_, bstack1111111ll11_opy_):
    try:
      working_dir = os.path.dirname(bstack1lllllll1l1l_opy_)
      shutil.unpack_archive(bstack1lllllll1l1l_opy_, working_dir)
      bstack1llllll1l1ll_opy_ = os.path.join(working_dir, bstack1111111ll11_opy_)
      os.chmod(bstack1llllll1l1ll_opy_, 0o755)
      return bstack1llllll1l1ll_opy_
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡵ࡯ࡼ࡬ࡴࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠦὋ"))
  def bstack1llllll11l1l_opy_(self):
    try:
      bstack111111111ll_opy_ = self.config.get(bstack11l111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪὌ"))
      bstack1llllll11l1l_opy_ = bstack111111111ll_opy_ or (bstack111111111ll_opy_ is None and self.bstack11l1l1l11l_opy_)
      if not bstack1llllll11l1l_opy_ or self.config.get(bstack11l111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨὍ"), None) not in bstack11l1l11l11l_opy_:
        return False
      self.bstack11l1l1ll11_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡩࡹ࡫ࡣࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣ὎").format(e))
  def bstack1111111ll1l_opy_(self):
    try:
      bstack1111111ll1l_opy_ = self.percy_capture_mode
      return bstack1111111ll1l_opy_
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡪࡺࡥࡤࡶࠣࡴࡪࡸࡣࡺࠢࡦࡥࡵࡺࡵࡳࡧࠣࡱࡴࡪࡥ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣ὏").format(e))
  def init(self, bstack11l1l1l11l_opy_, config, logger):
    self.bstack11l1l1l11l_opy_ = bstack11l1l1l11l_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1llllll11l1l_opy_():
      return
    self.bstack111111l1l1l_opy_ = config.get(bstack11l111_opy_ (u"ࠨࡲࡨࡶࡨࡿࡏࡱࡶ࡬ࡳࡳࡹࠧὐ"), {})
    self.percy_capture_mode = config.get(bstack11l111_opy_ (u"ࠩࡳࡩࡷࡩࡹࡄࡣࡳࡸࡺࡸࡥࡎࡱࡧࡩࠬὑ"))
    try:
      bstack1111111llll_opy_, bstack1111111ll11_opy_ = self.bstack1lllllll1lll_opy_()
      self.bstack111l1l11l11_opy_ = bstack1111111ll11_opy_
      bstack1llllll1l1ll_opy_, bstack1llllll1lll1_opy_ = self.bstack1llllll11lll_opy_(bstack1111111llll_opy_, bstack1111111ll11_opy_)
      if bstack1llllll1lll1_opy_:
        self.binary_path = bstack1llllll1l1ll_opy_
        thread = Thread(target=self.bstack1llllll11l11_opy_)
        thread.start()
      else:
        self.bstack1llllll1111l_opy_ = True
        self.logger.error(bstack11l111_opy_ (u"ࠥࡍࡳࡼࡡ࡭࡫ࡧࠤࡵ࡫ࡲࡤࡻࠣࡴࡦࡺࡨࠡࡨࡲࡹࡳࡪࠠ࠮ࠢࡾࢁ࠱ࠦࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡒࡨࡶࡨࡿࠢὒ").format(bstack1llllll1l1ll_opy_))
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧὓ").format(e))
  def bstack1llllllll111_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack11l111_opy_ (u"ࠬࡲ࡯ࡨࠩὔ"), bstack11l111_opy_ (u"࠭ࡰࡦࡴࡦࡽ࠳ࡲ࡯ࡨࠩὕ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack11l111_opy_ (u"ࠢࡑࡷࡶ࡬࡮ࡴࡧࠡࡲࡨࡶࡨࡿࠠ࡭ࡱࡪࡷࠥࡧࡴࠡࡽࢀࠦὖ").format(logfile))
      self.bstack1lllll1ll1ll_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸ࡫ࡴࠡࡲࡨࡶࡨࡿࠠ࡭ࡱࡪࠤࡵࡧࡴࡩ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤὗ").format(e))
  @measure(event_name=EVENTS.bstack11l1l1ll1ll_opy_, stage=STAGE.bstack1l111l11l_opy_)
  def bstack1llllll11l11_opy_(self):
    bstack1111111l1ll_opy_ = self.bstack1111111111l_opy_()
    if bstack1111111l1ll_opy_ == None:
      self.bstack1llllll1111l_opy_ = True
      self.logger.error(bstack11l111_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡶࡲ࡯ࡪࡴࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦ࠯ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽࠧ὘"))
      return False
    bstack1lllll1ll111_opy_ = [bstack11l111_opy_ (u"ࠥࡥࡵࡶ࠺ࡦࡺࡨࡧ࠿ࡹࡴࡢࡴࡷࠦὙ") if self.bstack11l1l1l11l_opy_ else bstack11l111_opy_ (u"ࠫࡪࡾࡥࡤ࠼ࡶࡸࡦࡸࡴࠨ὚")]
    bstack11111ll1ll1_opy_ = self.bstack1lllll1ll1l1_opy_()
    if bstack11111ll1ll1_opy_ != None:
      bstack1lllll1ll111_opy_.append(bstack11l111_opy_ (u"ࠧ࠳ࡣࠡࡽࢀࠦὛ").format(bstack11111ll1ll1_opy_))
    env = os.environ.copy()
    env[bstack11l111_opy_ (u"ࠨࡐࡆࡔࡆ࡝ࡤ࡚ࡏࡌࡇࡑࠦ὜")] = bstack1111111l1ll_opy_
    env[bstack11l111_opy_ (u"ࠢࡕࡊࡢࡆ࡚ࡏࡌࡅࡡࡘ࡙ࡎࡊࠢὝ")] = os.environ.get(bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭὞"), bstack11l111_opy_ (u"ࠩࠪὟ"))
    bstack1llllll1ll11_opy_ = [self.binary_path]
    self.bstack1llllllll111_opy_()
    self.bstack111111l1l11_opy_ = self.bstack11111111l11_opy_(bstack1llllll1ll11_opy_ + bstack1lllll1ll111_opy_, env)
    self.logger.debug(bstack11l111_opy_ (u"ࠥࡗࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠦὠ"))
    bstack11111111ll1_opy_ = 0
    while self.bstack111111l1l11_opy_.poll() == None:
      bstack1111111l111_opy_ = self.bstack1lllll1lllll_opy_()
      if bstack1111111l111_opy_:
        self.logger.debug(bstack11l111_opy_ (u"ࠦࡍ࡫ࡡ࡭ࡶ࡫ࠤࡈ࡮ࡥࡤ࡭ࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲࠢὡ"))
        self.bstack1llllllll1l1_opy_ = True
        return True
      bstack11111111ll1_opy_ += 1
      self.logger.debug(bstack11l111_opy_ (u"ࠧࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠤࡗ࡫ࡴࡳࡻࠣ࠱ࠥࢁࡽࠣὢ").format(bstack11111111ll1_opy_))
      time.sleep(2)
    self.logger.error(bstack11l111_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠬࠡࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠠࡇࡣ࡬ࡰࡪࡪࠠࡢࡨࡷࡩࡷࠦࡻࡾࠢࡤࡸࡹ࡫࡭ࡱࡶࡶࠦὣ").format(bstack11111111ll1_opy_))
    self.bstack1llllll1111l_opy_ = True
    return False
  def bstack1lllll1lllll_opy_(self, bstack11111111ll1_opy_ = 0):
    if bstack11111111ll1_opy_ > 10:
      return False
    try:
      bstack111111l11l1_opy_ = os.environ.get(bstack11l111_opy_ (u"ࠧࡑࡇࡕࡇ࡞ࡥࡓࡆࡔ࡙ࡉࡗࡥࡁࡅࡆࡕࡉࡘ࡙ࠧὤ"), bstack11l111_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰࡮ࡲࡧࡦࡲࡨࡰࡵࡷ࠾࠺࠹࠳࠹ࠩὥ"))
      bstack1111111l1l1_opy_ = bstack111111l11l1_opy_ + bstack11l1l11ll11_opy_
      response = requests.get(bstack1111111l1l1_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࠨὦ"), {}).get(bstack11l111_opy_ (u"ࠪ࡭ࡩ࠭ὧ"), None)
      return True
    except:
      self.logger.debug(bstack11l111_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡳࡨࡩࡵࡳࡴࡨࡨࠥࡽࡨࡪ࡮ࡨࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡪࡨࡥࡱࡺࡨࠡࡥ࡫ࡩࡨࡱࠠࡳࡧࡶࡴࡴࡴࡳࡦࠤὨ"))
      return False
  def bstack1111111111l_opy_(self):
    bstack111111l1ll1_opy_ = bstack11l111_opy_ (u"ࠬࡧࡰࡱࠩὩ") if self.bstack11l1l1l11l_opy_ else bstack11l111_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨὪ")
    bstack1111111lll1_opy_ = bstack11l111_opy_ (u"ࠢࡶࡰࡧࡩ࡫࡯࡮ࡦࡦࠥὫ") if self.config.get(bstack11l111_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧὬ")) is None else True
    bstack11ll11ll111_opy_ = bstack11l111_opy_ (u"ࠤࡤࡴ࡮࠵ࡡࡱࡲࡢࡴࡪࡸࡣࡺ࠱ࡪࡩࡹࡥࡰࡳࡱ࡭ࡩࡨࡺ࡟ࡵࡱ࡮ࡩࡳࡅ࡮ࡢ࡯ࡨࡁࢀࢃࠦࡵࡻࡳࡩࡂࢁࡽࠧࡲࡨࡶࡨࡿ࠽ࡼࡿࠥὭ").format(self.config[bstack11l111_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨὮ")], bstack111111l1ll1_opy_, bstack1111111lll1_opy_)
    if self.percy_capture_mode:
      bstack11ll11ll111_opy_ += bstack11l111_opy_ (u"ࠦࠫࡶࡥࡳࡥࡼࡣࡨࡧࡰࡵࡷࡵࡩࡤࡳ࡯ࡥࡧࡀࡿࢂࠨὯ").format(self.percy_capture_mode)
    uri = bstack11ll1l1l1_opy_(bstack11ll11ll111_opy_)
    try:
      response = bstack11ll11ll1l_opy_(bstack11l111_opy_ (u"ࠬࡍࡅࡕࠩὰ"), uri, {}, {bstack11l111_opy_ (u"࠭ࡡࡶࡶ࡫ࠫά"): (self.config[bstack11l111_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩὲ")], self.config[bstack11l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫέ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack11l1l1ll11_opy_ = data.get(bstack11l111_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪὴ"))
        self.percy_capture_mode = data.get(bstack11l111_opy_ (u"ࠪࡴࡪࡸࡣࡺࡡࡦࡥࡵࡺࡵࡳࡧࡢࡱࡴࡪࡥࠨή"))
        os.environ[bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࠩὶ")] = str(self.bstack11l1l1ll11_opy_)
        os.environ[bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࡢࡇࡆࡖࡔࡖࡔࡈࡣࡒࡕࡄࡆࠩί")] = str(self.percy_capture_mode)
        if bstack1111111lll1_opy_ == bstack11l111_opy_ (u"ࠨࡵ࡯ࡦࡨࡪ࡮ࡴࡥࡥࠤὸ") and str(self.bstack11l1l1ll11_opy_).lower() == bstack11l111_opy_ (u"ࠢࡵࡴࡸࡩࠧό"):
          self.bstack11l1l1111l_opy_ = True
        if bstack11l111_opy_ (u"ࠣࡶࡲ࡯ࡪࡴࠢὺ") in data:
          return data[bstack11l111_opy_ (u"ࠤࡷࡳࡰ࡫࡮ࠣύ")]
        else:
          raise bstack11l111_opy_ (u"ࠪࡘࡴࡱࡥ࡯ࠢࡑࡳࡹࠦࡆࡰࡷࡱࡨࠥ࠳ࠠࡼࡿࠪὼ").format(data)
      else:
        raise bstack11l111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡧࡧࡷࡧ࡭ࠦࡰࡦࡴࡦࡽࠥࡺ࡯࡬ࡧࡱ࠰ࠥࡘࡥࡴࡲࡲࡲࡸ࡫ࠠࡴࡶࡤࡸࡺࡹࠠ࠮ࠢࡾࢁ࠱ࠦࡒࡦࡵࡳࡳࡳࡹࡥࠡࡄࡲࡨࡾࠦ࠭ࠡࡽࢀࠦώ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡰࡦࡴࡦࡽࠥࡶࡲࡰ࡬ࡨࡧࡹࠨ὾").format(e))
  def bstack1lllll1ll1l1_opy_(self):
    bstack1lllllll11ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"ࠨࡰࡦࡴࡦࡽࡈࡵ࡮ࡧ࡫ࡪ࠲࡯ࡹ࡯࡯ࠤ὿"))
    try:
      if bstack11l111_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨᾀ") not in self.bstack111111l1l1l_opy_:
        self.bstack111111l1l1l_opy_[bstack11l111_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩᾁ")] = 2
      with open(bstack1lllllll11ll_opy_, bstack11l111_opy_ (u"ࠩࡺࠫᾂ")) as fp:
        json.dump(self.bstack111111l1l1l_opy_, fp)
      return bstack1lllllll11ll_opy_
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡣࡳࡧࡤࡸࡪࠦࡰࡦࡴࡦࡽࠥࡩ࡯࡯ࡨ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥᾃ").format(e))
  def bstack11111111l11_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1llllll1l11l_opy_ == bstack11l111_opy_ (u"ࠫࡼ࡯࡮ࠨᾄ"):
        bstack1llllll1ll1l_opy_ = [bstack11l111_opy_ (u"ࠬࡩ࡭ࡥ࠰ࡨࡼࡪ࠭ᾅ"), bstack11l111_opy_ (u"࠭࠯ࡤࠩᾆ")]
        cmd = bstack1llllll1ll1l_opy_ + cmd
      cmd = bstack11l111_opy_ (u"ࠧࠡࠩᾇ").join(cmd)
      self.logger.debug(bstack11l111_opy_ (u"ࠣࡔࡸࡲࡳ࡯࡮ࡨࠢࡾࢁࠧᾈ").format(cmd))
      with open(self.bstack1lllll1ll1ll_opy_, bstack11l111_opy_ (u"ࠤࡤࠦᾉ")) as bstack1lllll1llll1_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1lllll1llll1_opy_, text=True, stderr=bstack1lllll1llll1_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1llllll1111l_opy_ = True
      self.logger.error(bstack11l111_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡶࡥࡳࡥࡼࠤࡼ࡯ࡴࡩࠢࡦࡱࡩࠦ࠭ࠡࡽࢀ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠧᾊ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1llllllll1l1_opy_:
        self.logger.info(bstack11l111_opy_ (u"ࠦࡘࡺ࡯ࡱࡲ࡬ࡲ࡬ࠦࡐࡦࡴࡦࡽࠧᾋ"))
        cmd = [self.binary_path, bstack11l111_opy_ (u"ࠧ࡫ࡸࡦࡥ࠽ࡷࡹࡵࡰࠣᾌ")]
        self.bstack11111111l11_opy_(cmd)
        self.bstack1llllllll1l1_opy_ = False
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡴࡶࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡹ࡬ࡸ࡭ࠦࡣࡰ࡯ࡰࡥࡳࡪࠠ࠮ࠢࡾࢁ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࡿࢂࠨᾍ").format(cmd, e))
  def bstack1111lllll1_opy_(self):
    if not self.bstack11l1l1ll11_opy_:
      return
    try:
      bstack1lllllll1111_opy_ = 0
      while not self.bstack1llllllll1l1_opy_ and bstack1lllllll1111_opy_ < self.bstack1lllll1l1lll_opy_:
        if self.bstack1llllll1111l_opy_:
          self.logger.info(bstack11l111_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡳࡦࡶࡸࡴࠥ࡬ࡡࡪ࡮ࡨࡨࠧᾎ"))
          return
        time.sleep(1)
        bstack1lllllll1111_opy_ += 1
      os.environ[bstack11l111_opy_ (u"ࠨࡒࡈࡖࡈ࡟࡟ࡃࡇࡖࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓࠧᾏ")] = str(self.bstack1lllll1lll1l_opy_())
      self.logger.info(bstack11l111_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡵࡨࡸࡺࡶࠠࡤࡱࡰࡴࡱ࡫ࡴࡦࡦࠥᾐ"))
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡦࡶࡸࡴࠥࡶࡥࡳࡥࡼ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᾑ").format(e))
  def bstack1lllll1lll1l_opy_(self):
    if self.bstack11l1l1l11l_opy_:
      return
    try:
      bstack1llllll111ll_opy_ = [platform[bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩᾒ")].lower() for platform in self.config.get(bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᾓ"), [])]
      bstack1lllll1lll11_opy_ = sys.maxsize
      bstack1lllllll1l11_opy_ = bstack11l111_opy_ (u"࠭ࠧᾔ")
      for browser in bstack1llllll111ll_opy_:
        if browser in self.bstack1lllllll11l1_opy_:
          bstack1llllllll11l_opy_ = self.bstack1lllllll11l1_opy_[browser]
        if bstack1llllllll11l_opy_ < bstack1lllll1lll11_opy_:
          bstack1lllll1lll11_opy_ = bstack1llllllll11l_opy_
          bstack1lllllll1l11_opy_ = browser
      return bstack1lllllll1l11_opy_
    except Exception as e:
      self.logger.error(bstack11l111_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡪ࡮ࡴࡤࠡࡤࡨࡷࡹࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᾕ").format(e))
  @classmethod
  def bstack1111l11lll_opy_(self):
    return os.getenv(bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞࠭ᾖ"), bstack11l111_opy_ (u"ࠩࡉࡥࡱࡹࡥࠨᾗ")).lower()
  @classmethod
  def bstack11l11l1ll_opy_(self):
    return os.getenv(bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࡠࡅࡄࡔ࡙࡛ࡒࡆࡡࡐࡓࡉࡋࠧᾘ"), bstack11l111_opy_ (u"ࠫࠬᾙ"))
  @classmethod
  def bstack11lllllll1l_opy_(cls, value):
    cls.bstack11l1l1111l_opy_ = value
  @classmethod
  def bstack11111111111_opy_(cls):
    return cls.bstack11l1l1111l_opy_
  @classmethod
  def bstack11llllll111_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack1lllllll1ll1_opy_(cls):
    return cls.percy_build_id