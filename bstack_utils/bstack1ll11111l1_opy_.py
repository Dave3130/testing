# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l1l1l1111_opy_, bstack11l1l1l11l1_opy_, bstack11l1l111lll_opy_
import tempfile
import json
bstack11111ll1l1l_opy_ = os.getenv(bstack1lllll1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡇࡠࡈࡌࡐࡊࠨấ"), None) or os.path.join(tempfile.gettempdir(), bstack1lllll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡪࡥࡣࡷࡪ࠲ࡱࡵࡧࠣẦ"))
bstack11111ll1l11_opy_ = os.path.join(bstack1lllll1_opy_ (u"ࠢ࡭ࡱࡪࠦầ"), bstack1lllll1_opy_ (u"ࠨࡵࡧ࡯࠲ࡩ࡬ࡪ࠯ࡧࡩࡧࡻࡧ࠯࡮ࡲ࡫ࠬẨ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack1lllll1_opy_ (u"ࠩࠨࠬࡦࡹࡣࡵ࡫ࡰࡩ࠮ࡹࠠ࡜ࠧࠫࡲࡦࡳࡥࠪࡵࡠ࡟ࠪ࠮࡬ࡦࡸࡨࡰࡳࡧ࡭ࡦࠫࡶࡡࠥ࠳ࠠࠦࠪࡰࡩࡸࡹࡡࡨࡧࠬࡷࠬẩ"),
      datefmt=bstack1lllll1_opy_ (u"ࠪࠩ࡞࠳ࠥ࡮࠯ࠨࡨ࡙ࠫࡈ࠻ࠧࡐ࠾࡙࡚ࠪࠨẪ"),
      stream=sys.stdout
    )
  return logger
def bstack1l1l111l111_opy_():
  bstack11111llllll_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢࡈࡊࡈࡕࡈࠤẫ"), bstack1lllll1_opy_ (u"ࠧ࡬ࡡ࡭ࡵࡨࠦẬ"))
  return logging.DEBUG if bstack11111llllll_opy_.lower() == bstack1lllll1_opy_ (u"ࠨࡴࡳࡷࡨࠦậ") else logging.INFO
def bstack1ll11lllll1_opy_():
  global bstack11111ll1l1l_opy_
  if os.path.exists(bstack11111ll1l1l_opy_):
    os.remove(bstack11111ll1l1l_opy_)
  if os.path.exists(bstack11111ll1l11_opy_):
    os.remove(bstack11111ll1l11_opy_)
def bstack1ll11l1lll_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack11111ll1111_opy_ = log_level
  if bstack1lllll1_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩẮ") in config and config[bstack1lllll1_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪắ")] in bstack11l1l1l11l1_opy_:
    bstack11111ll1111_opy_ = bstack11l1l1l11l1_opy_[config[bstack1lllll1_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫẰ")]]
  if config.get(bstack1lllll1_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡺࡺ࡯ࡄࡣࡳࡸࡺࡸࡥࡍࡱࡪࡷࠬằ"), False):
    logging.getLogger().setLevel(bstack11111ll1111_opy_)
    return bstack11111ll1111_opy_
  global bstack11111ll1l1l_opy_
  bstack1ll11l1lll_opy_()
  bstack11111lllll1_opy_ = logging.Formatter(
    fmt=bstack1lllll1_opy_ (u"ࠫࠪ࠮ࡡࡴࡥࡷ࡭ࡲ࡫ࠩࡴࠢ࡞ࠩ࠭ࡴࡡ࡮ࡧࠬࡷࡢࡡࠥࠩ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨ࠭ࡸࡣࠠ࠮ࠢࠨࠬࡲ࡫ࡳࡴࡣࡪࡩ࠮ࡹࠧẲ"),
    datefmt=bstack1lllll1_opy_ (u"࡙ࠬࠫ࠮ࠧࡰ࠱ࠪࡪࡔࠦࡊ࠽ࠩࡒࡀࠥࡔ࡜ࠪẳ"),
  )
  bstack11111l1llll_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11111ll1l1l_opy_)
  file_handler.setFormatter(bstack11111lllll1_opy_)
  bstack11111l1llll_opy_.setFormatter(bstack11111lllll1_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11111l1llll_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack1lllll1_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠯ࡹࡨࡦࡩࡸࡩࡷࡧࡵ࠲ࡷ࡫࡭ࡰࡶࡨ࠲ࡷ࡫࡭ࡰࡶࡨࡣࡨࡵ࡮࡯ࡧࡦࡸ࡮ࡵ࡮ࠨẴ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11111l1llll_opy_.setLevel(bstack11111ll1111_opy_)
  logging.getLogger().addHandler(bstack11111l1llll_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11111ll1111_opy_
def bstack11111llll1l_opy_(config):
  try:
    bstack11111l1ll11_opy_ = set(bstack11l1l111lll_opy_)
    bstack11111ll1ll1_opy_ = bstack1lllll1_opy_ (u"ࠧࠨẵ")
    with open(bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫẶ")) as bstack1111l11111l_opy_:
      bstack11111ll11l1_opy_ = bstack1111l11111l_opy_.read()
      bstack11111ll1ll1_opy_ = re.sub(bstack1lllll1_opy_ (u"ࡴࠪࡢ࠭ࡢࡳࠬࠫࡂࠧ࠳࠰ࠤ࡝ࡰࠪặ"), bstack1lllll1_opy_ (u"ࠪࠫẸ"), bstack11111ll11l1_opy_, flags=re.M)
      bstack11111ll1ll1_opy_ = re.sub(
        bstack1lllll1_opy_ (u"ࡶࠬࡤࠨ࡝ࡵ࠮࠭ࡄ࠮ࠧẹ") + bstack1lllll1_opy_ (u"ࠬࢂࠧẺ").join(bstack11111l1ll11_opy_) + bstack1lllll1_opy_ (u"࠭ࠩ࠯ࠬࠧࠫẻ"),
        bstack1lllll1_opy_ (u"ࡲࠨ࡞࠵࠾ࠥࡡࡒࡆࡆࡄࡇ࡙ࡋࡄ࡞ࠩẼ"),
        bstack11111ll1ll1_opy_, flags=re.M | re.I
      )
    def bstack11111llll11_opy_(dic):
      bstack1111l111111_opy_ = {}
      for key, value in dic.items():
        if key in bstack11111l1ll11_opy_:
          bstack1111l111111_opy_[key] = bstack1lllll1_opy_ (u"ࠨ࡝ࡕࡉࡉࡇࡃࡕࡇࡇࡡࠬẽ")
        else:
          if isinstance(value, dict):
            bstack1111l111111_opy_[key] = bstack11111llll11_opy_(value)
          else:
            bstack1111l111111_opy_[key] = value
      return bstack1111l111111_opy_
    bstack1111l111111_opy_ = bstack11111llll11_opy_(config)
    return {
      bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬẾ"): bstack11111ll1ll1_opy_,
      bstack1lllll1_opy_ (u"ࠪࡪ࡮ࡴࡡ࡭ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ế"): json.dumps(bstack1111l111111_opy_)
    }
  except Exception as e:
    return {}
def bstack11111l1lll1_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack1lllll1_opy_ (u"ࠫࡱࡵࡧࠨỀ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11111lll1l1_opy_ = os.path.join(log_dir, bstack1lllll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡩ࡯࡯ࡨ࡬࡫ࡸ࠭ề"))
  if not os.path.exists(bstack11111lll1l1_opy_):
    bstack11111lll11l_opy_ = {
      bstack1lllll1_opy_ (u"ࠨࡩ࡯࡫ࡳࡥࡹ࡮ࠢỂ"): str(inipath),
      bstack1lllll1_opy_ (u"ࠢࡳࡱࡲࡸࡵࡧࡴࡩࠤể"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack1lllll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡥࡲࡲ࡫࡯ࡧࡴ࠰࡭ࡷࡴࡴࠧỄ")), bstack1lllll1_opy_ (u"ࠩࡺࠫễ")) as bstack11111lll1ll_opy_:
      bstack11111lll1ll_opy_.write(json.dumps(bstack11111lll11l_opy_))
def bstack11111ll111l_opy_():
  try:
    bstack11111lll1l1_opy_ = os.path.join(os.getcwd(), bstack1lllll1_opy_ (u"ࠪࡰࡴ࡭ࠧỆ"), bstack1lllll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡨࡵ࡮ࡧ࡫ࡪࡷ࠳ࡰࡳࡰࡰࠪệ"))
    if os.path.exists(bstack11111lll1l1_opy_):
      with open(bstack11111lll1l1_opy_, bstack1lllll1_opy_ (u"ࠬࡸࠧỈ")) as bstack11111lll1ll_opy_:
        bstack11111ll1lll_opy_ = json.load(bstack11111lll1ll_opy_)
      return bstack11111ll1lll_opy_.get(bstack1lllll1_opy_ (u"࠭ࡩ࡯࡫ࡳࡥࡹ࡮ࠧỉ"), bstack1lllll1_opy_ (u"ࠧࠨỊ")), bstack11111ll1lll_opy_.get(bstack1lllll1_opy_ (u"ࠨࡴࡲࡳࡹࡶࡡࡵࡪࠪị"), bstack1lllll1_opy_ (u"ࠩࠪỌ"))
  except:
    pass
  return None, None
def bstack11111ll11ll_opy_():
  try:
    bstack11111lll1l1_opy_ = os.path.join(os.getcwd(), bstack1lllll1_opy_ (u"ࠪࡰࡴ࡭ࠧọ"), bstack1lllll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡨࡵ࡮ࡧ࡫ࡪࡷ࠳ࡰࡳࡰࡰࠪỎ"))
    if os.path.exists(bstack11111lll1l1_opy_):
      os.remove(bstack11111lll1l1_opy_)
  except:
    pass
def bstack1l11l1l1_opy_(config):
  try:
    from bstack_utils.helper import bstack11l1111l_opy_, bstack1l111ll111_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack11111ll1l1l_opy_
    if config.get(bstack1lllll1_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡇࡵࡵࡱࡆࡥࡵࡺࡵࡳࡧࡏࡳ࡬ࡹࠧỏ"), False):
      return
    uuid = os.getenv(bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫỐ")) if os.getenv(bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬố")) else bstack11l1111l_opy_.get_property(bstack1lllll1_opy_ (u"ࠣࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠥỒ"))
    if not uuid or uuid == bstack1lllll1_opy_ (u"ࠩࡱࡹࡱࡲࠧồ"):
      return
    bstack11111lll111_opy_ = [bstack1lllll1_opy_ (u"ࠪࡶࡪࡷࡵࡪࡴࡨࡱࡪࡴࡴࡴ࠰ࡷࡼࡹ࠭Ổ"), bstack1lllll1_opy_ (u"ࠫࡕ࡯ࡰࡧ࡫࡯ࡩࠬổ"), bstack1lllll1_opy_ (u"ࠬࡶࡹࡱࡴࡲ࡮ࡪࡩࡴ࠯ࡶࡲࡱࡱ࠭Ỗ"), bstack11111ll1l1l_opy_, bstack11111ll1l11_opy_]
    bstack1111l1111ll_opy_, root_path = bstack11111ll111l_opy_()
    if bstack1111l1111ll_opy_ != None:
      bstack11111lll111_opy_.append(bstack1111l1111ll_opy_)
    if root_path != None:
      bstack11111lll111_opy_.append(os.path.join(root_path, bstack1lllll1_opy_ (u"࠭ࡣࡰࡰࡩࡸࡪࡹࡴ࠯ࡲࡼࠫỗ")))
    bstack1ll11l1lll_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack1lllll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠭࡭ࡱࡪࡷ࠲࠭Ộ") + uuid + bstack1lllll1_opy_ (u"ࠨ࠰ࡷࡥࡷ࠴ࡧࡻࠩộ"))
    with tarfile.open(output_file, bstack1lllll1_opy_ (u"ࠤࡺ࠾࡬ࢀࠢỚ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11111lll111_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11111llll1l_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11111l1ll1l_opy_ = data.encode()
        tarinfo.size = len(bstack11111l1ll1l_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11111l1ll1l_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack1lllll1_opy_ (u"ࠪࡨࡦࡺࡡࠨớ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack1lllll1_opy_ (u"ࠫࡷࡨࠧỜ")), bstack1lllll1_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲ࡼ࠲࡭ࡺࡪࡲࠪờ")),
        bstack1lllll1_opy_ (u"࠭ࡣ࡭࡫ࡨࡲࡹࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨỞ"): uuid
      }
    )
    bstack1111l1111l1_opy_ = bstack1l111ll111_opy_(cli.config, [bstack1lllll1_opy_ (u"ࠢࡢࡲ࡬ࡷࠧở"), bstack1lllll1_opy_ (u"ࠣࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠣỠ"), bstack1lllll1_opy_ (u"ࠤࡸࡴࡱࡵࡡࡥࠤỡ")], bstack11l1l1l1111_opy_)
    response = requests.post(
      bstack1lllll1_opy_ (u"ࠥࡿࢂ࠵ࡣ࡭࡫ࡨࡲࡹ࠳࡬ࡰࡩࡶ࠳ࡺࡶ࡬ࡰࡣࡧࠦỢ").format(bstack1111l1111l1_opy_),
      data=multipart_data,
      headers={bstack1lllll1_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪợ"): multipart_data.content_type},
      auth=(config[bstack1lllll1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧỤ")], config[bstack1lllll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩụ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack1lllll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡵࡱ࡮ࡲࡥࡩࠦ࡬ࡰࡩࡶ࠾ࠥ࠭Ủ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack1lllll1_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡱࡨ࡮ࡴࡧࠡ࡮ࡲ࡫ࡸࡀࠧủ") + str(e))
  finally:
    try:
      bstack1ll11lllll1_opy_()
      bstack11111ll11ll_opy_()
    except:
      pass